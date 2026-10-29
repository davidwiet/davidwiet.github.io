import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('mirror_blog', Path(__file__).resolve().parents[1] / 'scripts/mirror_blog.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def post(id=1, slug='published-essay'):
    return dict(id=id, slug=slug, title='Exact title', publication_id=m.PUBLICATION_ID,
                is_published=True, audience='everyone', type='newsletter',
                canonical_url=f'{m.SOURCE}/p/{slug}', post_date='2026-01-01T00:00:00Z',
                body_html='<p>Exact words &amp; punctuation. <a href="https://example.org/">Source</a></p>')


class Source:
    def __init__(self, posts):
        self.posts = posts
        self.fail = False

    def __call__(self, url):
        if '/api/v1/archive?' in url:
            offset = int(url.split('offset=')[1].split('&')[0])
            return json.dumps(self.posts[offset:offset + m.PAGE_SIZE])
        if self.fail:
            raise OSError('source unavailable')
        p = next(p for p in self.posts if p['canonical_url'] == url)
        return f'<link rel="canonical" href="{url}"><script id="preloads-json" type="application/json">{json.dumps({"post": p})}</script>'


class MirrorTests(unittest.TestCase):
    def test_exact_html_and_idempotent_atomic_snapshot(self):
        source = Source([post()])
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'posts.json'
            self.assertTrue(m.sync(dest, source))
            original = dest.read_bytes()
            self.assertFalse(m.sync(dest, source))
            self.assertEqual(dest.read_bytes(), original)
            self.assertEqual(json.loads(original)['posts'][0]['body_html'], post()['body_html'])
            source.posts[0]['body_html'] = '<p>Published correction.</p>'
            self.assertTrue(m.sync(dest, source))
            self.assertEqual(json.loads(dest.read_text())['posts'][0]['body_html'], '<p>Published correction.</p>')

    def test_archive_pagination_not_limited_to_rss_window(self):
        source = Source([post(i, f'article-{i}') for i in range(1, 42)])
        self.assertEqual(len(m.collect(source)['posts']), 41)

    def test_draft_future_preview_wrong_identity_and_missing_body_fail_closed(self):
        for change in [dict(is_published=False), dict(is_editor_preview=True),
                       dict(post_date='2999-01-01T00:00:00Z'), dict(publication_id=2),
                       dict(body_html=''), dict(free_unlock_required=True)]:
            with self.subTest(change=change):
                p = post(); p.update(change)
                with self.assertRaises((ValueError, KeyError)):
                    m.collect(Source([p]))

    def test_paid_posts_and_notes_are_not_mirrored(self):
        paid = post(2, 'paid'); paid['audience'] = 'only_paid'
        note = post(3, 'note'); note['type'] = 'thread'
        self.assertEqual([p['id'] for p in m.collect(Source([post(), paid, note]))['posts']], [1])
        self.assertEqual(m.collect(Source([paid]))['posts'], [])

    def test_rename_preserves_mirror_url_and_records_source_aliases(self):
        previous = m.collect(Source([post()]))
        current = m.collect(Source([post(slug='renamed')]), previous)['posts'][0]
        self.assertEqual(current['mirror_slug'], 'published-essay')
        self.assertEqual(current['source_url'], f'{m.SOURCE}/p/renamed')
        self.assertEqual(len(current['source_aliases']), 2)

    def test_complete_refresh_removes_withdrawn_post_and_does_not_duplicate(self):
        previous = m.collect(Source([post(), post(2, 'withdrawn')]))
        current = m.collect(Source([post()]), previous)
        self.assertEqual([p['id'] for p in current['posts']], [1])

    def test_partial_failure_empty_or_malformed_archive_preserves_previous_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'posts.json'
            source = Source([post()])
            m.sync(dest, source)
            original = dest.read_bytes()
            source.fail = True
            bad = [source, Source([]), lambda url: '<html>Unavailable</html>']
            for get in bad:
                with self.subTest(get=get):
                    with self.assertRaises((ValueError, OSError)):
                        m.sync(dest, get)
                    self.assertEqual(dest.read_bytes(), original)

    def test_repeated_archive_id_fails_instead_of_silently_truncating(self):
        with self.assertRaises(ValueError):
            m.collect(Source([post(), post()]))

    def test_unsafe_html_is_rejected_without_rewriting_prose(self):
        for body in ['<script>alert(1)</script>', '<img src="x" onerror="bad()">',
                     '<a href="javascript:bad()">Exact prose</a>']:
            p = post(); p['body_html'] = body
            with self.subTest(body=body), self.assertRaises(ValueError):
                m.collect(Source([p]))

    def test_slug_collision_fails(self):
        previous = m.collect(Source([post()]))
        with self.assertRaises(ValueError):
            m.collect(Source([post(slug='new-name'), post(2)]), previous)

    def test_agent_request_matches_published_revision_and_is_idempotent(self):
        request = dict(schema_version=1, request_id='post-1-revision-1', reason='significant-edit',
                       post_id=1, source_url=post()['canonical_url'],
                       expected_body_sha256=m.digest(post()['body_html']))
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / 'posts.json'
            self.assertTrue(m.sync(dest, Source([post()]), request=request))
            self.assertFalse(m.sync(dest, Source([post()]), request=request))
            self.assertEqual(json.loads(dest.read_text())['processed_request']['request_id'], request['request_id'])
            original = dest.read_bytes()
            request['expected_body_sha256'] = 'stale'
            with self.assertRaises(ValueError):
                m.sync(dest, Source([post()]), request=request)
            self.assertEqual(dest.read_bytes(), original)

    def test_request_for_unpublished_or_wrong_url_does_not_mark_completion(self):
        request = dict(schema_version=1, request_id='post-2', reason='publication',
                       post_id=2, source_url=f'{m.SOURCE}/p/not-live')
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                m.sync(Path(tmp) / 'posts.json', Source([post()]), request=request)


if __name__ == '__main__':
    unittest.main()
