#!/usr/bin/env python3
"""Check the HTML visitors and crawlers will actually receive after Astro builds."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.robotparser import RobotFileParser

from mirror_blog import BodyCheck, digest

ROOT = Path(__file__).resolve().parents[1]


class Rendered(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonical = []
        self.robots = []
        self.title = []
        self.in_title = False
        self.in_article_body = False
        self.div_depth = 0
        self.body_text = []
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical.append(attrs.get('href'))
        if tag == 'meta' and attrs.get('name') in {'robots', 'googlebot', 'bingbot'}:
            self.robots.append(attrs.get('content', ''))
        if tag == 'title':
            self.in_title = True
        if tag == 'div' and 'blog-body' in attrs.get('class', '').split():
            self.in_article_body = True
        if self.in_article_body:
            if tag == 'div':
                self.div_depth += 1
            if tag == 'a':
                self.links.append(attrs.get('href'))
            if tag == 'img':
                self.images.append((attrs.get('src'), attrs.get('alt')))

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        if self.in_article_body and tag == 'div':
            self.div_depth -= 1
            if self.div_depth == 0:
                self.in_article_body = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if self.in_article_body:
            self.body_text.append(data)


def verify(root=ROOT):
    archive = json.loads((root / 'content/blog/posts.json').read_text())
    status = json.loads((root / 'dist/blog/mirror-status.json').read_text())
    assert status['processed_request'] == archive.get('processed_request')
    assert {p['id']: p['body_sha256'] for p in status['posts']} == {
        p['id']: p['body_sha256'] for p in archive['posts']}
    robots = RobotFileParser()
    robots.parse((root / 'dist/robots.txt').read_text().splitlines())
    for post in archive['posts']:
        source = BodyCheck()
        source.feed(post['body_html'])
        assert digest(post['body_html']) == post['body_sha256']
        assert digest(''.join(source.text)) == post['text_sha256']
        page = root / 'dist/blog' / post['mirror_slug'] / 'index.html'
        markup = page.read_text()
        rendered = Rendered()
        rendered.feed(markup)
        assert rendered.canonical == [post['source_url']], page
        assert not any('noindex' in value or 'nofollow' in value for value in rendered.robots), page
        # Astro minifies HTML, so compare every decoded text node with whitespace
        # normalized only. The archived source HTML itself is byte-for-byte exact.
        normalize = lambda text: re.sub(r'\s+', ' ', text).strip()
        assert normalize(''.join(rendered.body_text)) == normalize(''.join(source.text)), page
        assert post['title'] in ''.join(rendered.title), page
        expected = Rendered()
        expected.feed('<div class="blog-body">' + post['body_html'] + '</div>')
        assert rendered.links == expected.links, page
        assert rendered.images == expected.images, page
        for bot in ['OAI-SearchBot', 'ChatGPT-User', 'Googlebot', 'bingbot']:
            assert robots.can_fetch(bot, f"https://davidwiet.github.io/blog/{post['mirror_slug']}/"), bot
        data = re.search(r'<script type="application/ld\+json">(.*?)</script>', markup, re.S)
        assert data and json.loads(data[1])['headline'] == post['title'], page
    print(f"Verified {len(archive['posts'])} built articles: prose, titles, links, images, canonical URLs, structured data and crawler access")


if __name__ == '__main__':
    verify()
