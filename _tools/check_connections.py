#!/usr/bin/env python3
"""Check generated routes, page metadata, local links and guide coverage."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from connection_catalog import PROVIDERS

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.ids=set(); self.links=[]; self.h1=0; self.title=0; self.description=False
        self.private_inputs=[]
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, 'Duplicate id '+a['id']
            self.ids.add(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'title': self.title += 1
        if tag == 'meta' and a.get('name') == 'description': self.description=bool(a.get('content'))
        if tag in ('a','script','link','img'):
            self.links.append(a.get('href') or a.get('src') or '')
        if tag == 'input' and a.get('type') == 'password': self.private_inputs.append(a)

pages={p:Page(p.read_text()) for p in (ROOT/'connections').rglob('*.html')}
expected={ROOT/'connections'/'index.html'}|{ROOT/'connections'/p['slug']/'index.html' for p in PROVIDERS}
assert set(pages)==expected, 'Missing or obsolete guide routes'
count=0
for path,page in pages.items():
    assert page.h1==page.title==1 and page.description, path
    assert not page.private_inputs, 'Documentation must not collect passwords'
    for link in page.links:
        parsed=urlsplit(link)
        if parsed.scheme or parsed.netloc: continue
        target=(ROOT/unquote(parsed.path).lstrip('/')) if parsed.path.startswith('/') else (path.parent/unquote(parsed.path)) if parsed.path else path
        if target.is_dir(): target=target/'index.html'
        assert target.is_file(), f'{path}: broken link {link}'
        if parsed.fragment:
            target_page=pages.get(target) or Page(target.read_text())
            assert unquote(parsed.fragment) in target_page.ids, f'{path}: missing anchor {link}'
        count+=1
directory=(ROOT/'connections'/'index.html').read_text()
for provider in PROVIDERS:
    assert '/connections/'+provider['slug']+'/' in directory
    assert provider['sources'] and all(url.startswith('https://') for _,url in provider['sources'])
assert 'ibkr ib gateway tws' in directory, 'Common IBKR search alias missing'
for landing in ('index.html','start.html'):
    assert '/connections/' in (ROOT/landing).read_text(), 'Guide navigation missing'
print(f'Passed: {len(PROVIDERS)} provider guides, directory metadata, {count} local links/anchors, credential-free pages and navigation.')
