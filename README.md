[README.md](https://github.com/user-attachments/files/31404441/README.md)
<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logo/alpharch-mark-dark.svg">
  <img src="logo/alpharch-mark-light.svg" alt="Alpharch" width="140">
</picture>

# ALPHARCH

**A Linux operating system for the futures trader.**

*pronounced alpha-arch*

[![Status](https://img.shields.io/badge/status-blueprint-e8a33d?style=flat-square)](https://alpharch.org)
[![Built on](https://img.shields.io/badge/built%20on-Omarchy-9a6b14?style=flat-square)](https://omarchy.org)
[![Base](https://img.shields.io/badge/base-Arch%20%C2%B7%20Hyprland-1d6f47?style=flat-square)](https://archlinux.org)
[![License](https://img.shields.io/badge/license-MIT-555?style=flat-square)](LICENSE)

### Linux is for traders.

*The exchanges run Linux. Now you do.*

**[alpharch.org](https://alpharch.org)**

</div>

---

## Status: blueprint

**Alpharch is not installable yet.** There is no ISO, no install script, and no release. What exists today is a complete, public design specification and a working visual storyboard — the whole system described in enough detail to build it.

This repository will grow into the real thing in the open. If you want to watch that happen, star the repo; if you want to help, see [Contributing](#contributing).

---

## What it is

Every trading session has the same shape: the same charts in the same places, the same execution platform, the same research, at the same times, every day. Alpharch treats that shape as the operating system's job.

By **07:30** it has written *The Daily* — your desk sheet, with the overnight session, key levels and their confluences, the dealer positioning map, the expected move, and a plan skeleton drawn from your own playbook file. At **08:00**, one keypress raises the entire desk: footprints on the first workspace, execution on the second, research on the third, the flow tape on the fifth. Monitors arrange. Data goes live. When the bell rings you are reading the market, not arranging windows.

It is built for the trader who reads **order flow and options flow** — footprints, the book, sweeps, dark pool prints, gamma exposure — and whose home market is **futures**.

## The flagship: The Narrator

No one can watch the footprint, the order book, the options tape and the internals at once. The Narrator can, and does, all session long.

It sits on the same event streams as every chart on the desk. When you ask — by voice, hands never leaving the ladder — it answers in seconds, in the vocabulary of your own playbook:

> **You** · *"flow check"*
>
> **The Narrator** — *"Last twelve minutes: two absorption events at 6428, the overnight high held both times. CVD is diverging on this push. Zero-DTE call volume is building at 6440 and the wall has migrated up. TICK averaging +420, bonds bid, NQ leading. Your A-setup zone sits five points below."*

**The fence, which is architecture and not a setting:** the Narrator holds read-only streams and has no path to the order ticket. It describes; it never advises. No signals, no picks, no "AI that trades for you" — ever. A tape-reading assistant that makes calls is a signal service with your account attached, and this one is built so it cannot become one.

## Planned capabilities

| Area | What ships |
|---|---|
| **Futures-native** | `trade-symbol` launcher over the CME/CBOT/NYMEX/COMEX catalog · automatic front-month resolution and roll countdowns · a session clock that thinks in Globex, not "market hours" · tick value, margin and R-sizing first-class in the ticket |
| **Order flow** | Footprint + cumulative delta + volume profile as the default chart workspace (MotiveWave native, Sierra Chart under Wine) · large-lot, iceberg and pulled-liquidity detection · absorption and CVD-divergence alerts tied to your marked levels · crypto footprints computed locally from free exchange websockets |
| **Options flow** | Live sweep/block/dark-pool tape · a GEX engine computing call wall, put wall and gamma flip before the open and refreshing intraday as 0DTE volume rebuilds the landscape · dealer-hedging estimates on level breaks |
| **The desk** | `trade-desk` one-key assembly and teardown · `trade-journal` with chart capture · `trade-focus` (the anti-tilt switch) · `trade-flow` / `trade-gex` · alerts and econ calendar |
| **Feedback loop** | Auto-journaling of every fill with full market context · personal analytics ("your VAH-reclaim long wins 68% when cumulative TICK is positive at entry") · *The Debrief* after the close · journal-linked replay · OS-enforced daily loss limits |
| **Battlestation** | Full Omarchy theme inheritance plus a semantic trading contract · curated themes (The Pit, Quotron, Globex, Paper, Tape) · session-aware switching · colorblind-safe direction palettes in every theme · describe a theme to the agent and it builds it |

Full detail lives in the [blueprint](https://alpharch.org).

## The mission

The matching engines at the CME run Linux. The banks' infrastructure runs Linux. The quant funds run Linux. Every other technical profession — developers, scientists, engineers — moved to open tools years ago and never looked back.

The one person in the entire chain still locked in is the retail trader: closed-source platforms, rented by the month, auditable by no one, running on the one operating system built for someone else's business model.

Alpharch exists to end that arrangement, and to build the **Linux-based trading community** that ends it. Everything here is open source and forkable — the desk, the themes, the commands, eventually the playbook format itself — because a trader's tools should be owned, inspected and improved by traders.

## What we will not pretend

- **On latency.** Retail order flow travels hundreds of milliseconds to a broker, and no kernel patch changes that. What ships instead is what matters at that distance: truthful clocks, a machine that never sleeps mid-session, a power-failure plan.
- **On Windows-only platforms.** Some trading software will never run on Linux. IBKR runs natively here, TradingView runs accelerated, Sierra Chart runs well under a tested compatibility layer — but Quantower, NinjaTrader and their class stay on Windows, and we say so here rather than in a footnote.
- **On data.** Real depth and live options flow are paid feeds. The free tier is honest about being an approximation rather than dressing it up.
- **On tilt.** The P&L readout ships disabled. Watching unrealized P&L all day is how accounts die; turning it on is a decision, not a default.
- **On the assistant.** It analyzes everything and advises on nothing.

## Built on Omarchy

Alpharch is a friendly fork of [Omarchy](https://omarchy.org) — the opinionated, AI-native Arch Linux desktop released in 2025 by David Heinemeier Hansson, now backed by its own foundation. The installer, update pipeline, theme engine and agent framework are theirs and stay theirs; we track upstream and keep the trading layer as an additive overlay.

We build the one thing they never will: the trading desk on top. Themes and generally useful fixes go back upstream.

## Roadmap

| Phase | Deliverable |
|---|---|
| **P0** | The trading overlay on stock Omarchy — desk assembly, workspaces, The Pit, the symbol switcher. *The desk works.* |
| **P1** | Theme set and the hardened `trade-*` command family · `alphad` v1 (data service). *Installable by a stranger via script.* |
| **P2** | Bar widgets · data providers · the GEX engine and flow tape · tape detectors · auto-journaling · agent skills. *The screenshots that sell it.* |
| **P3** | The actual fork: ISO, installer integration, migrations · The Debrief, analytics, replay, risk guardian, first working Narrator. |
| **P4** | Public launch, docs, community. |

Beyond 1.0: **The Gym** (replay the whole desk through historical sessions and trade them in sim), **The Archive** (a queryable memory of your entire trading career), **The Playbook Standard** (an open format for trading rules), **The Floor** (a private desk room for people you trust), **The Pocket & The Panel**.

## Contributing

The project is pre-alpha and the most useful contributions right now are **ideas, critique, and domain expertise** — especially from traders who read flow.

- **Open an issue** if a workflow in the blueprint is wrong, missing, or would break at a real desk.
- **Traders:** what does your morning actually look like? What would make the desk assemble *your* way?
- **Linux folks:** theme submissions, Hyprland/Quickshell expertise, packaging.
- **Quants:** the GEX engine, footprint detection, and journal analytics are where the interesting math lives.

Please keep discussion in the open. No signals, no trade calls, no "what should I buy" — that is not what this project is for, and it never will be.

## About this repository

This repo currently holds the [alpharch.org](https://alpharch.org) site — a single self-contained `index.html`, no build step. The distribution itself lands here as P0 completes.

## License

MIT. Use it, fork it, ship it.

## Disclaimer

Alpharch is software, not financial advice. It provides tools, never signals. Nothing in this project or its documentation is a recommendation to buy or sell anything. Trading futures and options involves substantial risk of loss.

<div align="center">

---

**Linux is for traders.**

</div>
