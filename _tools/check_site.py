#!/usr/bin/env python3
"""Validate published page links, image types and screenshot gallery targets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.ids, self.links, self.images = set(), [], []
        self.headings = self.titles = 0
        self.description = False
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            assert attrs['id'] not in self.ids, f"Duplicate id: {attrs['id']}"
            self.ids.add(attrs['id'])
        self.headings += tag == 'h1'
        self.titles += tag == 'title'
        if tag == 'meta' and attrs.get('name') == 'description':
            self.description = bool(attrs.get('content'))
        if tag in ('a', 'link', 'script', 'img'):
            self.links.append(attrs.get('href') or attrs.get('src') or '')
        if tag == 'img':
            assert 'alt' in attrs, 'Image missing alt text'
            assert int(attrs.get('width', 0)) > 0 and int(attrs.get('height', 0)) > 0
            self.images.append(attrs['src'])
        assert not (tag == 'input' and attrs.get('type') == 'password'), 'No credential collection'


pages = {path: Page(path) for path in ROOT.rglob('*.html') if '.git' not in path.parts}
count = 0
for path, page in pages.items():
    assert page.headings == page.titles == 1 and page.description, path
    for link in page.links:
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        target = (ROOT / unquote(parsed.path).lstrip('/')) if parsed.path.startswith('/') else (path.parent / unquote(parsed.path)) if parsed.path else path
        target = target.resolve()
        assert target.is_relative_to(ROOT), f'Link escapes site: {link}'
        if target.is_dir():
            target /= 'index.html'
        assert target.is_file(), f'{path.name}: missing {link}'
        if parsed.fragment:
            assert target in pages and unquote(parsed.fragment) in pages[target].ids, f'Missing anchor: {link}'
        count += 1

for path in (ROOT / 'images').iterdir():
    signature = path.read_bytes()[:8]
    assert (path.suffix == '.png' and signature == b'\x89PNG\r\n\x1a\n') or (path.suffix == '.jpg' and signature[:3] == b'\xff\xd8\xff'), path
for src in re.findall(r"src:'(/images/[^']+)'", (ROOT / 'site.js').read_text()):
    assert (ROOT / src.lstrip('/')).is_file(), f'Missing gallery image: {src}'
print(f'Passed: {len(pages)} pages, {count} local links/anchors, image signatures, metadata and gallery assets.')
