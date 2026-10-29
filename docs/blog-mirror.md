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
There is no schedule or polling. Its mirror job alone uses the repository's ephemeral
`GITHUB_TOKEN` with `contents: write`; build/deploy retain existing permissions.
It commits only `content/blog/posts.json`. Build checks out the resulting commit
and deploys in the same workflow: a bot-token push does not itself trigger Pages.
No GitHub account or repository security setting changes are required.

After verified publication or a significant public edit, the existing publishing
agent commits `content/blog/refresh-request.json` through its existing GitHub
connector. This push starts the same workflow. The request file is the most recent
public refresh trigger, not a queue, scheduler or separate store. The source adapter
always uses the fixed publication URL; request content cannot select another source
or execute commands. Significant edits include public prose/title, source links,
intentional images/credits and canonical URL changes; draft work and cosmetic saves
do not qualify. Preserve the agent's current Shabbat and publication safeguards.

The connector exposes GitHub file commits, but not workflow dispatch. Use its
`fetch_file` and `update_file` with the fresh blob SHA; use `create_file` only when
the path is confirmed absent. Use branch `main`, repository
`davidwiet/davidwiet.github.io`, and commit message `Refresh blog mirror: <title>`.
Read the existing request before retrying an uncertain write. Reuse the same
`request_id` for the same publication/edit; do not duplicate a completed request.

```json
{
  "schema_version": 1,
  "request_id": "post-222456624-published-revision-identifier",
  "reason": "significant-edit",
  "post_id": 222456624,
  "source_url": "https://davidwiet.substack.com/p/choosing-ai-models",
  "expected_body_sha256": null
}
```

`reason` is `publication`, `significant-edit`, or the one-time `initial-backfill`.
When exact current public `body_html` is available, put its SHA-256 in
`expected_body_sha256`; otherwise use null and require complete current-public-text
comparison in the receipt. Never hash local draft prose as a published revision.
The job refuses to complete if the requested public post/URL or expected HTML
revision is absent. It records the processed request in the verified snapshot.

Verify the actual run at the repository's Actions runs, then read
`https://davidwiet.github.io/blog/mirror-status.json`: its `processed_request.request_id`
must equal the request, and its post hash must match the verified source snapshot.
Check the actual article URL, full text, links and image rendering. A successful
request commit alone is not mirror completion. Record the request, commit/run,
live URL, source hash and outcome in the existing publication receipt. On failure
keep the public article intact, retain the blocker and recover this same request;
never republish/resend it or add a timer. Native **Run workflow** remains available
for an explicitly requested recovery.

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
