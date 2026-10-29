# The Human Image mirror

Substack owns published article text, title, dates, links and media. Local
`Technology_Blog` drafts and editorial candidates are never mirror inputs.
The existing Pages workflow owns public acquisition, Git history and deployment;
there is no extra service, agent, account, secret or paid dependency.

The architectural decision joins two positive aims: broader readable distribution
and exact editorial/source ownership. KEEP the existing repository and Pages
workflow; MERGE acquisition, versioning and deployment into that workflow; KEEP
the mirror job's write permission separate from the reader build; DEFER a new
repository, scheduler, authenticated API or webhook bridge. The public snapshot
is a rebuildable publication copy, not an authoring store. A new post, a corrected
post, a renamed slug and an unavailable source are the required change/failure
scenarios. Tests below check each one before deployment.

`python3 scripts/mirror_blog.py` reads the complete paginated, unauthenticated
public archive and each public article. Only published, unrestricted newsletter
articles from publication 10948199 are accepted. The original `body_html` is
stored unchanged in `content/blog/posts.json`, with native post ID, current source
URL, prior source URLs, publication/update dates and SHA-256 digests. The snapshot
excludes the rest of Substack's page data. A public post remains published source
even when a newer local revision is awaiting author review.

`/blog/<first-mirrored-slug>/` stays stable across source slug/title changes;
native post ID prevents duplicate imports. Complete successful refreshes remove
withdrawn/restricted entries. A completely empty archive is treated as a possible
upstream error and requires investigation before removing the final mirror.
Network, schema, identity, partial-download and unsafe-HTML failures leave the
last verified snapshot and deployed site intact. Git commits preserve recovery
versions. Embedded platform interaction controls are hidden by CSS; article
prose, image credits, source links and HTML remain intact.

The public archive endpoint and `preloads-json` are observed Substack interfaces,
not a supported API contract. Schema changes fail visibly in Actions; they must
be repaired before automatic refresh resumes. There is no authenticated fallback
and no attempt to retrieve drafts, subscriber records or private/paid content.

## Running and verification

The existing **Deploy to GitHub Pages** workflow runs on pushes and manual dispatch.
There is no schedule or polling. The publishing executor acquires and verifies the
public source, then commits `content/blog/posts.json` through the existing GitHub
connector. GitHub validates that supplied snapshot, builds and deploys the exact
triggering commit. It uses only the existing read/Pages permissions; no write token,
new account, secret or repository security-setting change is required.

The live GitHub test on 29 October 2026 demonstrated that its hosted runner could
not fetch Substack (curl HTTP failure, run 40949581307). The same complete public
source fetch succeeded on David's Mac. Acquisition therefore belongs to the
existing source-accessing publishing executor, immediately after verified native
publication or a significant live edit. The CI runner never substitutes drafts or
silently treats a stale saved snapshot as a fresh source read.

Significant edits include public prose/title, source links, intentional images and
credits, or canonical URL changes. Draft work and cosmetic saves do not qualify.
The publisher uses a current checkout of this repository; preserve the existing
snapshot before refreshing so native post IDs retain their established mirror URLs.
For example, after confirming the actual post ID and current canonical live URL:

```sh
python3 scripts/mirror_blog.py --event-id post-222456624-revision-identifier \
  --reason significant-edit --post-id 222456624 \
  --source-url https://davidwiet.substack.com/p/choosing-ai-models
```

Use `publication` for a new public article or `initial-backfill` for the one-time
initial copy. Reuse the same event ID when recovering the same operation. When
exact current public HTML was independently captured, optionally supply its hash
with `--expected-body-sha256`; never hash a local draft as a published revision.
The collector verifies the complete public archive and every article before
writing atomically. It refuses a missing post/URL or a stale expected revision.

Commit only the resulting `content/blog/posts.json` through GitHub's `fetch_file`
and `update_file` tools using the fresh blob SHA, branch `main`, repository
`davidwiet/davidwiet.github.io`, and message `Mirror blog: <title>`. Use `create_file`
only for a confirmed missing snapshot. The connector's public snapshot commit
triggers the existing Pages workflow; no workflow-dispatch tool or trigger file is
needed. Inspect existing remote content before retrying an uncertain write. A
cloud manager unable to fetch Substack must obtain the verified snapshot from the
current publishing executor via its existing handoff. If that route is unavailable,
report the exact source/dispatch blocker; do not claim automatic coverage.

Verify Actions success, then read
`https://davidwiet.github.io/blog/mirror-status.json`: its
`processed_request.request_id` must equal the event ID and its post hash must match
the newly verified snapshot. Check the actual article's full text, links and images.
A successful snapshot commit alone is not mirror completion. Record event ID,
commit/run, live URL, source hash and outcome in the existing publication receipt.
On failure preserve the Substack publication and recover this same operation;
never republish/resend it or add a timer. Preserve existing Shabbat and single-writer
safeguards. Native **Run workflow** remains available for explicit recovery of an
already committed verified snapshot.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/mirror_blog.py --check
npm ci
npm run build
python3 scripts/verify_blog.py
```

Regression checks cover full pagination beyond the RSS window, exact transfer,
updates, idempotence, slug changes, restrictions, withdrawal, duplicate IDs,
unsafe HTML and preservation after partial failures. Built-page verification
compares all decoded prose, link targets and image URLs/alt text with the source
snapshot, as well as canonical tags, structured data and crawler rules.

## Search and canonical policy

Article copies link to and declare their current Substack originals as canonical.
This preserves existing publication ownership and consolidates duplicate URLs;
it can cause search engines to prefer Substack over the mirror in search results.
The blog archive and existing research pages are self-canonical and included in
`/sitemap.xml`; noncanonical article copies remain ordinary HTML links in the
archive. `/robots.txt` permits crawlers, including OAI-SearchBot. Public access,
structured data and a sitemap do not prove indexing, ranking or AI citation.
Changing which domain is the primary publication would be a separate decision.

## Recovery

To pause agent-triggered refresh, suspend that step in the existing publisher.
To restore a bad
public snapshot, restore `content/blog/posts.json` from a verified Git commit and
fix/pause the source acquisition before rebuilding. A normal push refreshes the
source again. To retire the mirror, remove its workflow job and blog routes/data;
retain the existing research routes and release-evidence workflow.

Technical references: [GitHub workflow triggering](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow),
[canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).
