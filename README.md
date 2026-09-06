# Alpharch website

Source for [alpharch.org](https://alpharch.org), served by GitHub Pages from `main` at the repository root. Alpharch is an additive trading overlay for Omarchy Linux. Application development lives in [alpharch-linux/alpharch](https://github.com/alpharch-linux/alpharch).

- `index.html`: front page with real development-desk screenshots, starting layouts and explicit release status.
- `start.html`: public-preview manual, including the installed live desk.
- `theme.css`: shared white, ink and brass website palette and typography.
- `site.css`, `site.js`: page presentation, screenshot selection and install-command copying.
- `images/`: actual application captures, plus the explicitly decorative After Hours wallpaper. Chart screenshots contain no generated or illustrative market data.
- `connections/`: searchable directory and individual provider guides.
- `install`: public bootstrap. Documentation changes do not release application worktree changes.

## Maintain connection guides

Edit `_tools/connection_catalog.py`, then run:

```sh
python3 _tools/build_connections.py
python3 _tools/check_connections.py
node --check connections/guides.js
```

The generator writes static pages and `_data/connections.json`. JavaScript enhances directory search and filtering; every provider guide remains readable without it. The underscore-prefixed authoring directories are not website routes.

Each guide records its review date, official sources, account route, Linux feasibility, prerequisites and actual Alpharch readiness. Never infer a working Alpharch integration from a provider API existing. Broker/FCM accounts are distinct from data/routing connections. Public market data is distinct from private account access and order execution.

IBKR supplies native Linux TWS and IB Gateway. Cross-platform web protocols elsewhere are integration possibilities, not claims of native desktop support or completed Omarchy acceptance testing.

The existing public tools include Coinbase spot, Hyperliquid perpetual data, Deribit options, and legacy Binance parsers subject to regional access. The 1.8.0-alpha.1 public preview adds the redesigned chart desk, Kraken public spot and the futures CSV importer. The included IBKR bridge remains experimental and requires account acceptance; no broker execution is supported.

The website collects no credentials. Keep passwords, keys, account identifiers and private research out of pages and source data. Link to current official terms for fees and eligibility.

## Local preview

```sh
python3 -m http.server 17864 --bind 127.0.0.1
```

Open `http://127.0.0.1:17864/connections/`. Production retains GitHub Pages and the existing CNAME; no hosting migration is required.

## Screenshot provenance and copy review

Refreshed September 6, 2026 against the working application and existing command implementations. `desk.png` and `studies.png` are the September 5 real-data captures from the development desk; `bitcoin-desk.jpg` and `starting-desks.jpg` were captured September 6 through the browser at its actual visible width. The gallery captions identify dates and the fact these are static public-market captures. Original screenshot bytes are retained.

The public installer ships the redesigned chart desk in 1.8.0-alpha.1. Keep its preview status and the separate futures/account acceptance limits beside installation instructions. App release: https://github.com/alpharch-linux/alpharch/releases/tag/v1.8.0-alpha.1. The existing Daily (`trade-brief`) is an on-demand morning brief; automatic scheduling, a full overnight futures report and dealer positioning are not implemented by it.

Run `python3 _tools/check_bootstrap.py`, `python3 _tools/check_site.py`, `python3 _tools/check_connections.py`, and `node --check site.js` before publication. Update screenshot alt text, dimensions, caption and full-size links together when replacing a capture.

The website uses a light editorial theme across the home page, manual and connection guides. Actual chart screenshots retain the application’s own colors. The existing light-surface logo variant is used in all headers. Keep foreground/background pairs consistent with `theme.css` when extending a page.

Futures and crypto are both core product audiences. Keep ES/NQ visible while stating IBKR gateway acceptance and other provider adapter work accurately. Crypto screenshots document working public feeds; they do not narrow the product roadmap. The planned hosted Desk Brain subscription is an optional paid service. Do not advertise subscriptions, checkout or a price as available until they actually launch; current local features and the user-owned Claude CLI path remain available.

After Hours is the bundled Alpharch desktop wallpaper, shown in a centered, viewport-aware home-page section with a PNG download. It is generated brand artwork based on the existing logo, separate from the real-data chart screenshots. Its original 1672 × 941 PNG is displayed without cropping; keep those dimensions and the download link aligned when replacing it.

The wallpaper preview is capped at 60rem and at the small viewport height in width (roughly 56% of viewport height for the full 16:9 artwork). Keep its original aspect ratio and allow the caption to wrap. The homepage and manual use a versioned stylesheet URL to avoid stale browser CSS after this layout fix.
