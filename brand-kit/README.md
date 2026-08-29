# Brand Kit — Aligned KPIs™ / 1 to 100 Advisors, Inc.

One mark carries the whole brand. The company, the product, and the app all use
the **identical symbol** — only the name beside it changes. That symbol is the constant.

Copy this entire `brand-kit/` folder into any project to keep everything in sync.
The canonical source is `assets/` in the marketing site repo; this folder mirrors it.

## What the mark means

| Element | Meaning |
| ------- | ------- |
| **Flywheel** — two equal 147° arcs, open at the lower left and upper right | Continual progress. The circle is broken on purpose so it reads as *turning*, not closed. |
| **Four pillars** — ascending bars, rising in height and tone | Visibility · Intelligence · Alignment · Better Results |
| **Trend line + plane** — green, climbing above the bars and out through the opening | Growth that clears the numbers and keeps going |

Green appears once and only once, on the trend line.

## Files

Each logo ships as a scalable **.svg** (use this in apps and on the web) plus a
high-resolution **.png** (for slides, Word, email, and anywhere SVG isn't supported).

| Logo | Light backgrounds | Dark backgrounds |
|------|-------------------|------------------|
| Shared symbol (mark only) | `symbol-light.svg` | `symbol-dark.svg` |
| Aligned KPIs™ — horizontal | `aligned-kpis-light.svg` | `aligned-kpis-dark.svg` |
| Aligned KPIs™ — stacked | `aligned-kpis-stacked-light.svg` | `aligned-kpis-stacked-dark.svg` |
| 1 to 100 Advisors, Inc. — horizontal | `1to100-advisors-light.svg` | `1to100-advisors-dark.svg` |
| 1 to 100 Advisors, Inc. — stacked | `1to100-advisors-stacked-light.svg` | `1to100-advisors-stacked-dark.svg` |
| App icon (rounded square) | `app-icon-light.svg` | `app-icon-dark.svg` |
| Favicon (simplified) | `favicon.svg` — adapts to dark mode on its own | |

**Light vs. dark:** use the *light* files on white/light backgrounds and the *dark*
files on dark backgrounds. If your app supports light/dark mode, swap on theme.

**Which lockup:** horizontal is the workhorse — site header, email signature, documents.
Stacked is for square-ish spaces: social avatars, slide title cards, sponsor walls.
The symbol alone is for app tiles and anywhere the name is already nearby.

**The favicon is not the full mark.** At 16px the four pillars merge into a smear, so
`favicon.svg` keeps the flywheel, the two tallest pillars, and the trend line, with
heavier strokes, and recolors itself for dark browser tabs. It is the one sanctioned
simplification — don't invent others.

**Company vs. product:** use **Aligned KPIs™** for everything customer-facing. Use
**1 to 100 Advisors, Inc.** only where corporate identification is appropriate —
contracts, About, footer, invoices.

## Color palette

Light-background logos:
- Navy `#16314F` · Blue `#2178C4` · Pillar tints `#9BC2E4` → `#64A1D5` → `#2178C4` → `#16314F`
- Growth green `#6FB52C` · Muted text `#6E6E73`

Dark-background logos:
- Ice `#AEC2DA` · Blue `#2178C4` · Pillar tints `#2178C4` → `#64A1D5` → `#9BC2E4` → `#FFFFFF`
- Growth green `#6FB52C` · Text `#FFFFFF` / `#AEC2DA`

## Typography

The wordmarks are **outlined paths, not live text**, so they render identically on
every machine and in every application. They are set in **Lato** (SIL Open Font
License): Bold for *Aligned KPIs*, Light and Regular for *1 TO 100 / ADVISORS, INC.*

Never re-typeset a wordmark. Use the file.

## Usage notes

- Prefer the **.svg** — it stays sharp at any size.
- **Clear space:** at least 25% of the mark's height on all sides. The files are
  cropped tight to the artwork, so measure from the file's edge.
- **Minimum size:** the mark holds together down to about **24px**. Below that the
  pillars merge — use a simplified favicon instead.
- Don't recolor, rotate, stretch, outline, add effects to, or reorder the elements.
- Don't put the light version on a dark background, or the reverse.
- Don't redraw the mark by hand. Every coordinate is solved geometry — scale the SVG.

## Animation

Each element carries a stable ID (`#ak-flywheel-navy`, `#ak-flywheel-blue`,
`#ak-pillars` / `.ak-pillar`, `#ak-trend-line`, `#ak-trend-plane`), so the mark
animates without being rebuilt. The canonical sequence: the plane enters at the
lower-left opening, orbits the flywheel once tracing each arc as it passes, the
pillars rise beneath it, then it banks out of the orbit, climbs across the bars
drawing the trend line behind it, and parks at the tip.

The plane is defined in its own frame (nose forward on +x, origin at the trend
line's endpoint: `M 20 4.5 L -20 -17.5 L -8 4.5 Z`), so one motion path plus
`rotate="auto"` flies it — it banks through every turn on its own.

See `logo-mark-preview.html` in the marketing site repo for a working demo.

## Retired

The **CEO Operating System™** name is retired and must not appear in any marketing,
product, or sales material. Its logo files have been deleted from this kit.
Never use "Executive Reporting Platform" as the category, either — reporting is a
capability, not our identity. The category is **Executive Visibility Platform**.
