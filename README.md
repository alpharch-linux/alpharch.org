# Alpharch website

Source for [alpharch.org](https://alpharch.org), served by GitHub Pages from `main` at the repository root. Alpharch is an additive trading overlay for Omarchy Linux. Application development lives in [alpharch-linux/alpharch](https://github.com/alpharch-linux/alpharch).

- `index.html`: front page with real development-desk screenshots, starting layouts and explicit release status.
- `start.html`: public-preview manual, including the installed live desk.
- `theme.css`: shared white, ink and brass website palette and typography.
- `site.css`, `site.js`: page presentation, screenshot selection and install-command copying.
- `images/`: actual application captures, plus the explicitly decorative After Hours wallpaper. Chart screenshots contain no generated or illustrative market data.
- `videos/alpharch-hyprland-desktop-v2.mp4`: the 47-second Hyprland desktop film, featured at `/#film`. H.264/AAC, 1920 × 1080, with the logo intro, original music and edited loading transitions. The poster is a frame from the real source recording. Playback is user-initiated, with native controls, inline mobile playback, a download link and a text description. No video data is preloaded before playback.
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

Refreshed September 8, 2026. The home page leads with the Hyprland edition and makes Omarchy the explicit platform in the headline, metadata, foundation note and installation path. Classic remains an option, not the lead gallery.

`hyprland-desk-20260908.jpg`, `hyprland-chart-focus-20260908.jpg` and `hyprland-order-flow-20260908.jpg` are fresh 1920 × 1080 desktop captures of the installed application on September 8. They show native Hyprland windows with actual public Coinbase BTC/USD data: the three-window desk, a focused candle chart with a keyboard-placed horizontal level, and a heatmap with trade bubbles and RSI. JPEG encoding is the only image processing. The source captures are `Alpharch-Hyprland-2026-09-08.png`, `Alpharch-Chart-Focus-2026-09-08.png` and `Alpharch-Order-Flow-2026-09-08.png` in the authoring workspace outputs. The new `hyprland-starting-desks-20260908.png` is a 1280 × 800 browser capture from the installed chart service, with Hyprland selected and the real Three.js opening logo visible. Application changes are published on main through `dbb1c14`. No market data is fabricated or composited. Dates, alt text, dimensions and full-size links match each asset. Earlier images remain at their existing URLs for compatibility.

The film and its poster still show the September 6 recording. Its caption makes that date explicit and points to the updated screenshot gallery. The manual includes focused chart commands, keyboard drawing placement, native window resizing, saved chart themes and independent Omarchy window styling.

The manual now describes the main chooser on every launch, native shortcuts and saved desks, plus the distinction between per-window Hyprland replay and shared-clock Classic replay. The current installer follows public main and includes changes newer than the initial 1.8.0-alpha.1 tag; do not imply that the original tagged release includes all later Hyprland changes.

The public installer ships the redesigned chart desk in 1.8.0-alpha.1. Keep its preview status and the separate futures/account acceptance limits beside installation instructions. App release: https://github.com/alpharch-linux/alpharch/releases/tag/v1.8.0-alpha.1. The existing Daily (`trade-brief`) is an on-demand morning brief; automatic scheduling, a full overnight futures report and dealer positioning are not implemented by it.

Run `python3 _tools/check_bootstrap.py`, `python3 _tools/check_site.py`, `python3 _tools/check_connections.py`, and `node --check site.js` before publication. Update screenshot alt text, dimensions, caption and full-size links together when replacing a capture.

The website uses a light editorial theme across the home page, manual and connection guides. Actual chart screenshots retain the application’s own colors. The existing light-surface logo variant is used in all headers. Keep foreground/background pairs consistent with `theme.css` when extending a page.

Futures and crypto are both core product audiences. Keep ES/NQ visible while stating IBKR gateway acceptance and other provider adapter work accurately. Crypto screenshots document working public feeds; they do not narrow the product roadmap. The planned hosted Desk Brain subscription is an optional paid service. Do not advertise subscriptions, checkout or a price as available until they actually launch; current local features and the user-owned Claude CLI path remain available.

After Hours is the bundled Alpharch desktop wallpaper, shown in a centered, viewport-aware home-page section with a PNG download. It is generated brand artwork based on the existing logo, separate from the real-data chart screenshots. Its original 1672 × 941 PNG is displayed without cropping; keep those dimensions and the download link aligned when replacing it.

The wallpaper preview is capped at 60rem and at the small viewport height in width (roughly 56% of viewport height for the full 16:9 artwork). Keep its original aspect ratio and allow the caption to wrap. The homepage and manual use a versioned stylesheet URL to avoid stale browser CSS after this layout fix.
