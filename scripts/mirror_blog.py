#!/usr/bin/env python3
"""Mirror only the unauthenticated, published Substack archive. No credentials.

The public archive endpoint is undocumented. Fail closed if its schema changes;
never substitute local drafts or an authenticated response.
"""
import argparse
import hashlib
import json
import re
import subprocess
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

SOURCE = "https://davidwiet.substack.com"
PUBLICATION_ID = 10948199
PAGE_SIZE = 20
ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def fetch(url):
    if urlsplit(url).netloc != "davidwiet.substack.com":
        raise ValueError("Unexpected source host")
    result = subprocess.run(
        ["curl", "--silent", "--show-error", "--fail", "--location",
         "--proto", "=https", "--proto-redir", "=https", "--max-redirs", "3",
         "--max-time", "45", "--retry", "2", "--user-agent", "Mozilla/5.0",
         url], check=True, capture_output=True,
    )
    if len(result.stdout) > 10 * 1024 * 1024:
        raise ValueError("Unexpectedly large public response")
    return result.stdout.decode("utf-8")


class Preloads(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.inside = False
        self.parts = []
        self.canonicals = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script" and attrs.get("id") == "preloads-json":
            self.inside = True
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals.append(attrs.get("href"))

    def handle_endtag(self, tag):
        if tag == "script":
            self.inside = False

    def handle_data(self, data):
        if self.inside:
            self.parts.append(data)


class BodyCheck(HTMLParser):
    """Reject active content instead of silently changing the author's HTML."""
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "iframe", "object", "embed", "form", "input",
                   "base", "meta", "link", "style", "foreignobject"}:
            raise ValueError(f"Unsupported active article element: {tag}")
        for key, value in attrs:
            if key.startswith("on") or key in {"srcdoc", "action", "formaction"}:
                raise ValueError(f"Unsupported article attribute: {key}")
            if key in {"href", "src", "xlink:href"} and value:
                value = re.sub(r"[\x00-\x20]", "", value).lower()
                if urlsplit(value).scheme not in {"", "http", "https", "mailto", "tel"}:
                    raise ValueError("Unsupported article URL scheme")

    handle_startendtag = handle_starttag

    def handle_data(self, data):
        self.text.append(data)


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def validate_snapshot(snapshot):
    if (snapshot.get("schema_version") != 1 or snapshot.get("publication_id") != PUBLICATION_ID
            or snapshot.get("source") != SOURCE or not isinstance(snapshot.get("posts"), list)):
        raise ValueError("Unexpected published snapshot identity/schema")
    ids, slugs = set(), set()
    for post in snapshot["posts"]:
        if (type(post.get("id")) is not int or post["id"] in ids or
                not SLUG.fullmatch(post.get("mirror_slug", "")) or
                post["mirror_slug"] in slugs or
                not SLUG.fullmatch(post.get("source_slug", "")) or
                post.get("source_url") != f"{SOURCE}/p/{post['source_slug']}" or
                not post.get("title")):
            raise ValueError("Invalid/duplicate public post identity or URL")
        ids.add(post["id"]); slugs.add(post["mirror_slug"])
        if datetime.fromisoformat(post["published_at"].replace("Z", "+00:00")) > datetime.now(timezone.utc):
            raise ValueError("Future-dated snapshot")
        body = post.get("body_html", "")
        check = BodyCheck(); check.feed(body)
        if (not "".join(check.text).strip() or digest(body) != post.get("body_sha256") or
                digest("".join(check.text)) != post.get("text_sha256")):
            raise ValueError("Public snapshot content/hash verification failed")
    return snapshot


def archive(get):
    posts = []
    seen = set()
    for page in range(1000):
        batch = json.loads(get(
            f"{SOURCE}/api/v1/archive?sort=new&offset={page * PAGE_SIZE}&limit={PAGE_SIZE}"
        ))
        if not isinstance(batch, list) or len(batch) > PAGE_SIZE:
            raise ValueError("Unexpected public archive schema")
        for post in batch:
            if not isinstance(post, dict) or type(post.get("id")) is not int:
                raise ValueError("Missing public post identity")
            if post["id"] in seen:
                raise ValueError("Archive pagination repeated a post; retry a fresh snapshot")
            seen.add(post["id"])
            posts.append(post)
        if len(batch) < PAGE_SIZE:
            return posts
    raise ValueError("Public archive pagination exceeded limit")


def collect(get=fetch, previous=None):
    old = {p["id"]: p for p in (previous or {}).get("posts", [])}
    posts = []
    paths = set()
    entries = archive(get)
    if not entries:
        raise ValueError("Empty public archive; refusing to erase the mirror")
    for entry in entries:
        # Paid previews, Notes, scheduled posts and drafts are never input.
        if entry.get("audience") != "everyone" or entry.get("type") != "newsletter":
            continue
        slug = entry.get("slug", "")
        if not SLUG.fullmatch(slug):
            raise ValueError("Invalid source slug")
        url = f"{SOURCE}/p/{slug}"
        if entry.get("canonical_url") != url:
            raise ValueError("Archive canonical URL differs from publication URL")
        parser = Preloads()
        parser.feed(get(url))
        data = json.loads("".join(parser.parts))
        post = data["post"]
        if (post.get("id") != entry["id"] or
                post.get("publication_id") != PUBLICATION_ID or
                post.get("is_published") is not True or
                post.get("is_editor_preview") is True or
                post.get("is_geoblocked") is True or
                post.get("audience") != "everyone" or
                post.get("type") != "newsletter" or
                post.get("free_unlock_required") is True or
                post.get("canonical_url") != url or parser.canonicals != [url]):
            raise ValueError(f"Public identity/access verification failed: {url}")
        date = datetime.fromisoformat(post["post_date"].replace("Z", "+00:00"))
        if date > datetime.now(timezone.utc):
            raise ValueError("Future-dated article cannot be mirrored")
        body = post.get("body_html")
        if not isinstance(body, str) or not body.strip() or not post.get("title"):
            raise ValueError("Public article body/title missing; preserve last verified mirror")
        check = BodyCheck()
        check.feed(body)
        if not "".join(check.text).strip():
            raise ValueError("Article has no readable text")
        prior = old.get(post["id"], {})
        # The first mirrored slug owns this ID's URL, even after a Substack rename.
        mirror_slug = prior.get("mirror_slug", slug)
        if not SLUG.fullmatch(mirror_slug) or mirror_slug in paths:
            raise ValueError("Invalid or colliding stable mirror URL")
        paths.add(mirror_slug)
        posts.append({
            "id": post["id"], "title": post["title"],
            "subtitle": post.get("subtitle") or "",
            "description": post.get("description") or "",
            "author": "David Wietchner", "published_at": post["post_date"],
            "source_updated_at": post.get("updated_at"),
            "source_url": url, "source_slug": slug, "mirror_slug": mirror_slug,
            "source_aliases": sorted(set(prior.get("source_aliases", []) +
                                         [prior.get("source_url", url), url])),
            "body_sha256": digest(body), "text_sha256": digest("".join(check.text)),
            "body_html": body,
        })
    return {"schema_version": 1, "publication_id": PUBLICATION_ID,
            "source": SOURCE, "posts": sorted(posts, key=lambda p: p["published_at"], reverse=True)}


def sync(destination, get=fetch, check=False, request=None):
    previous = json.loads(destination.read_text()) if destination.exists() else None
    # Complete every fetch and validation before writing anything. Network/schema
    # failures leave the entire previous snapshot intact, including removed posts.
    current = collect(get, previous)
    if request is not None:
        if (not isinstance(request, dict) or request.get("schema_version") != 1 or
                not isinstance(request.get("request_id"), str) or
                not 1 <= len(request["request_id"]) <= 200 or
                request.get("reason") not in {"initial-backfill", "publication", "significant-edit"}):
            raise ValueError("Invalid agent mirror request")
        matching = [p for p in current["posts"] if p["id"] == request.get("post_id") and
                    p["source_url"] == request.get("source_url")]
        if len(matching) != 1:
            raise ValueError("Requested public post/URL is absent from verified source")
        expected = request.get("expected_body_sha256")
        if expected is not None and expected != matching[0]["body_sha256"]:
            raise ValueError("Requested public revision is not yet visible; refusing stale completion")
        current["processed_request"] = {k: request[k] for k in
                                        ["request_id", "reason", "post_id", "source_url"]}
    validate_snapshot(current)
    encoded = json.dumps(current, ensure_ascii=False, indent=2) + "\n"
    changed = not destination.exists() or destination.read_text() != encoded
    if changed and not check:
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_suffix(".tmp")
        temporary.write_text(encoded, encoding="utf-8")
        temporary.replace(destination)
    print(f"{len(current['posts'])} verified public posts; changed={str(changed).lower()}")
    return changed


if __name__ == "__main__":
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument("--check", action="store_true", help="Validate live content; do not write")
    args.add_argument("--destination", type=Path, default=ROOT / "content/blog/posts.json")
    args.add_argument("--verify-snapshot", action="store_true", help="Validate saved snapshot offline; do not fetch or write")
    args.add_argument("--event-id")
    args.add_argument("--reason", choices=["initial-backfill", "publication", "significant-edit"])
    args.add_argument("--post-id", type=int)
    args.add_argument("--source-url")
    args.add_argument("--expected-body-sha256")
    options = args.parse_args()
    if options.verify_snapshot:
        validate_snapshot(json.loads(options.destination.read_text()))
        print("Saved public snapshot identity, safe HTML and complete hashes verified")
    else:
        request = None
        if any([options.event_id, options.reason, options.post_id, options.source_url]):
            if not all([options.event_id, options.reason, options.post_id, options.source_url]):
                args.error("event-id, reason, post-id and source-url must be supplied together")
            request = dict(schema_version=1, request_id=options.event_id, reason=options.reason,
                           post_id=options.post_id, source_url=options.source_url,
                           expected_body_sha256=options.expected_body_sha256)
        sync(options.destination, check=options.check, request=request)
