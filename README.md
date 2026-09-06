# Alpharch website

Source for [alpharch.org](https://alpharch.org), served by GitHub Pages from `main` at the repository root. Alpharch is an additive trading overlay for Omarchy Linux. Application development lives in [alpharch-linux/alpharch](https://github.com/alpharch-linux/alpharch).

- `index.html`: front page with real development-desk screenshots, starting layouts and explicit release status.
- `start.html`: public-tools manual plus labeled development-desk instructions.
- `site.css`, `site.js`: shared presentation, screenshot selection and install-command copying.
- `images/`: actual development-build captures; no generated or illustrative market charts.
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

The existing public tools include Coinbase spot, Hyperliquid perpetual data, Deribit options, and legacy Binance parsers subject to regional access. The redesigned chart desk and Databento CSV importer are separate development work. No live broker adapter is advertised as released.

The website collects no credentials. Keep passwords, keys, account identifiers and private research out of pages and source data. Link to current official terms for fees and eligibility.

## Local preview

```sh
python3 -m http.server 17864 --bind 127.0.0.1
```

Open `http://127.0.0.1:17864/connections/`. Production retains GitHub Pages and the existing CNAME; no hosting migration is required.

## Screenshot provenance and copy review

Refreshed September 6, 2026 against the working application and existing command implementations. `desk.png` and `studies.png` are the September 5 real-data captures from the development desk; `bitcoin-desk.jpg` and `starting-desks.jpg` were captured September 6 through the browser at its actual visible width. The gallery captions identify dates and the fact these are static public-market captures. Original screenshot bytes are retained.

The public installer does not yet ship the redesigned chart desk. Keep that distinction beside screenshots and installation instructions until the application release actually changes. The existing Daily (`trade-brief`) is an on-demand morning brief; automatic scheduling, a full overnight futures report and dealer positioning are not implemented by it.

Run `python3 _tools/check_site.py`, `python3 _tools/check_connections.py`, and `node --check site.js` before publication. Update screenshot alt text, dimensions, caption and full-size links together when replacing a capture.
