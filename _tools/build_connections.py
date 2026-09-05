#!/usr/bin/env python3
"""Build static connection guides for the existing GitHub Pages website."""
import html
import json
from pathlib import Path
from connection_catalog import PROVIDERS, REVIEWED

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'connections'
STATUSES = {
    'development': ('Live feed verified · development', 'Live public data has passed checks in the development desk. This is not yet a claim about the public installer or authenticated account access.'),
    'existing': ('Available in existing tools', 'Public data is available in the existing Alpharch tools. Account linking and broker execution are separate features.'),
    'limited': ('Existing tool · access limited', 'The legacy adapter remains in Alpharch, but this feed was not reachable from the test location. It is not offered in the new desk.'),
    'planned': ('Adapter not released', 'The provider offers an integration route. Alpharch does not yet offer a working connection for it.'),
    'access': ('Integration & provider access required', 'Alpharch still needs an implemented, tested adapter and any required provider approval. Having an account alone does not enable this connection.'),
    'verify': ('Account route needs verification', 'The correct API route or account permissions have not been fully verified. There is no working Alpharch connection to claim here.'),
}
E = html.escape

def shell(title, description, path, body):
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)} · Alpharch</title><meta name="description" content="{E(description)}">
<link rel="canonical" href="https://alpharch.org{path}"><link rel="icon" href="/alpharch-favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/connections/style.css"><script src="/connections/guides.js" defer></script>
</head><body><a class="skip" href="#main">Skip to content</a>
<header class="mast"><a class="brand" href="/" aria-label="Alpharch home"><img src="/alpharch-mark-dark.svg" width="38" height="38" alt="">ALPHARCH<span>.</span></a>
<nav aria-label="Main"><a href="/start.html">The manual</a><a href="/connections/" aria-current="{'page' if path == '/connections/' else 'false'}">Connections</a><a href="https://github.com/alpharch-linux/alpharch">Source ↗</a></nav></header>
{body}
<footer><a class="brand" href="/">ALPHARCH<span>.</span></a><p>The trading layer for Omarchy Linux.</p><p>Provider facts reviewed <time datetime="{REVIEWED}">September 5, 2026</time>.<br>Software support is stated separately from provider capability. Provider names do not imply partnership or certification.</p><a href="/connections/">All connection guides ↑</a></footer>
</body></html>'''

def source_links(p):
    return ''.join(f'<li><a href="{E(url)}" rel="noopener noreferrer">{E(label)} ↗</a></li>' for label,url in p['sources'])

def build():
    OUT.mkdir(exist_ok=True)
    lookup = {p['slug']:p for p in PROVIDERS}
    assert len(lookup) == len(PROVIDERS), 'Duplicate provider URL'
    for p in PROVIDERS:
        label, state = STATUSES[p['status']]
        related = ''.join(f'<a href="/connections/{slug}/">{E(lookup[slug]["name"])} →</a>' for slug in p['related'])
        steps = ''.join(f'<li><h3>{E(heading)}</h3><p>{E(text)}</p></li>' for heading,text in p['steps'])
        trouble = ''.join(f'<details><summary>{E(heading)}</summary><p>{E(text)}</p></details>' for heading,text in p['trouble'])
        needs = ''.join(f'<li>{E(item)}</li>' for item in p['needs'])
        body = f'''<main id="main" class="guide"><div class="breadcrumbs"><a href="/connections/">Connections</a><span>/</span>{E(p['category'])}</div>
<div class="guide-grid"><article><header class="guide-head"><p class="eyebrow">How to connect</p><h1>{E(p['name'])}<span class="period">.</span></h1><p class="lead">{E(p['summary'])}</p></header>
<div class="readiness {p['status']}"><span class="status-label">Alpharch support</span><strong>{E(label)}</strong><p>{E(state)}</p></div>
<section id="prepare"><h2>Before you start</h2><ul class="needs">{needs}</ul></section>
<section id="steps"><h2>{'Connect the existing tool' if p['status']=='existing' else 'Prepare your connection'}</h2><ol class="steps">{steps}</ol></section>
<section id="troubleshooting"><h2>If something is missing</h2>{trouble}</section>
<section id="sources"><h2>Official instructions</h2><p>Provider setup can change. These sources support the provider facts above; Alpharch support comes from its own implementation review.</p><ul class="sources">{source_links(p)}</ul></section>
{f'<section class="related"><h2>Follow your data route</h2>{related}</section>' if related else ''}
</article><aside><div class="aside-inner"><p class="eyebrow">Connection notes</p><dl><dt>Provider type</dt><dd>{E(p['category'])}</dd><dt>Connection route</dt><dd>{E(p['route'])}</dd><dt>Linux</dt><dd>{E(p['linux'])}</dd><dt>Reviewed</dt><dd>September 5, 2026</dd></dl>
<nav aria-label="On this page"><a href="#prepare">Before you start</a><a href="#steps">Connection steps</a><a href="#troubleshooting">Troubleshooting</a><a href="#sources">Official instructions</a></nav>
<p class="aside-note">This is a setup guide. Sign-in happens through a supported connection in the installed application or on the provider’s own authorization page. This website never asks for broker credentials.</p><button type="button" class="print-button" id="printGuide">Print this guide</button></div></aside></div></main>'''
        dest = OUT/p['slug']; dest.mkdir(exist_ok=True)
        (dest/'index.html').write_text(shell('Connect '+p['name'],p['summary'],'/connections/'+p['slug']+'/',body))
    sections = []
    for category in ('Futures brokers','Data & routing','Crypto exchanges'):
        rows = []
        for p in PROVIDERS:
            if p['category'] != category: continue
            status = STATUSES[p['status']][0]
            rows.append(f'''<a class="provider" href="/connections/{p['slug']}/" data-category="{E(category)}" data-status="{p['status']}" data-search="{E(' '.join([p['name'],p['route'],p['linux'],p['aliases']]).lower())}"><span class="provider-name">{E(p['name'])}<small>{E(p['route'])}</small></span><span class="provider-status {p['status']}">{E(status)}</span><span class="arrow" aria-hidden="true">↗</span></a>''')
        sections.append(f'<section class="provider-section" data-section="{E(category)}"><h2>{E(category)}</h2><div class="provider-list">'+''.join(rows)+'</div></section>')
    body = f'''<main id="main" class="directory"><div class="intro"><div><p class="eyebrow">The connection manual</p><h1>Your broker.<br>Your Linux desk<span class="period">.</span></h1></div><p class="lead">Find the right data connection for your charts. Linux setup, account requirements and the current state of every integration, in one place.</p></div>
<div class="directory-tools"><label class="search-label" for="providerSearch">Find your provider<input id="providerSearch" type="search" placeholder="Search broker, exchange or data feed…" autocomplete="off"></label><div class="filter-wrap"><label for="categoryFilter">Market</label><select id="categoryFilter"><option value="">All providers</option><option>Futures brokers</option><option>Data &amp; routing</option><option>Crypto exchanges</option></select></div><label class="available-filter"><input id="availableOnly" type="checkbox">Existing Alpharch tools only</label></div>
<p class="result-count" id="resultCount" role="status" aria-live="polite">{len(PROVIDERS)} provider guides</p>
<noscript><p>Search needs JavaScript. Every provider guide remains available below.</p></noscript>
<div class="directory-grid"><div>{''.join(sections)}<p id="noResults" hidden>No providers match. Clear the search or choose another market.</p></div>
<aside><div class="aside-inner"><h2>Start with your feed.</h2><p>Your broker holds the account. Your feed supplies the prices. Sometimes they use different logins.</p><p>AMP, EdgeClear and other futures brokers can supply a route such as Rithmic or CQG. Read the broker page first, then follow the matching feed guide.</p><div class="aside-callout"><strong>IBKR runs on Linux.</strong><p>TWS and IB Gateway have official Linux downloads. The Alpharch adapter still needs implementation and account testing.</p><a href="/connections/interactive-brokers/">Read the IBKR guide →</a></div>
<h3>What works today?</h3><p>The existing tools read public Coinbase and Hyperliquid feeds and Deribit options. The separate development chart desk has verified Coinbase, Hyperliquid and Kraken feeds for BTC, ETH and SOL. Live broker connections are not released.</p><a href="#data-basics">Understand the data ↓</a></div></aside></div>
<section id="data-basics" class="data-basics"><p class="eyebrow">Know what reaches your chart</p><h2>A login is only the beginning.</h2><div class="data-grid"><div><span class="data-number">01</span><h3>Quotes</h3><p>Top-of-book shows the best bid and ask. It does not establish a full depth feed.</p></div><div><span class="data-number">02</span><h3>Trades &amp; depth</h3><p>Footprints need trade events. Heatmaps need book updates. Check the feed’s detail, history and limits.</p></div><div><span class="data-number">03</span><h3>Individual orders</h3><p>Market-by-order and aggregated depth are different. A Level-2 label is not a promise of individual-order data.</p></div></div><p>Futures exchange subscriptions and provider access may cost extra. Alpharch’s software license does not include those services. Check the current terms linked in each guide.</p><p class="scope-note">Coverage: major retail futures routes and a broad crypto exchange set. This directory is a researched connection map, not a claim to support every broker. No login or trading credentials are collected here.</p></section></main>'''
    (OUT/'index.html').write_text(shell('Broker & exchange connection guides','How to connect futures brokers and crypto data feeds on Linux. Official setup routes and honest Alpharch integration status.','/connections/',body))
    (ROOT/'_data'/'connections.json').write_text(json.dumps(PROVIDERS,indent=2,ensure_ascii=False)+'\n')
    print(f'Built directory and {len(PROVIDERS)} provider guides.')

if __name__ == '__main__': build()
