# Renew IT Resources — HPE Nimble Inventory & Used-Value Estimate

**Inventory date:** 2026-07-07
**Prepared for:** justalink357@gmail.com

## Contents
| File | Description |
|------|-------------|
| `HPE_Nimble_Asset_Inventory.csv` | Original asset inventory (as supplied) — 9 HPE Nimble arrays |
| `HPE_Nimble_Used_Price_Estimate_2026-07-07__Used_Price_Estimate.csv` | Estimated used / secondary-market values |
| `HPE_Nimble_Used_Price_Estimate_2026-07-07__Sources_Methodology.csv` | Sources & methodology notes |
| `README.md` | This summary |

> Spreadsheets are stored as CSV so they render as tables directly on GitHub. Open `../../csv-viewer.html` (e.g. via GitHub Pages) for an in-browser viewer/editor.

## What "used account" pricing means here
Fair-market **secondary / refurbished** value for each **base dual-controller array as configured**. Figures are anchored to live refurbished-dealer and eBay listings (July 2026), then scaled by raw capacity, controller class, and expansion shelves. All values are **USD** and exclude shipping, tax, active HPE support/InfoSight renewal, professional services, and any resident data.

> All nine arrays carry a HW End-of-Support date of **7/31/2028** — still HPE-supportable, which sustains resale demand today.

## Estimated used values

| # | S/N | DC | Model | Type | Shelves | HDD (TB) | SSD (TB) | Low | **Point** | High |
|---|-----|----|-------|------|--------:|--------:|--------:|----:|-------:|-----:|
| 1 | 0862 | DDC1 | HF40 | Hybrid | – | 126 | 11.52 | $15,000 | **$16,875** | $18,000 |
| 2 | 4469 | DDC1 | AF60 | All-Flash | 1 | – | 253 | $42,000 | **$47,000** | $52,000 |
| 3 | 7343 | DDC1 | AF60 | All-Flash | 1 | – | 184 | $33,000 | **$37,000** | $41,000 |
| 4 | 8949 | DDC1 | AF60 | All-Flash | 0 | – | 184 | $31,000 | **$34,950** | $38,000 |
| 5 | 4349 | HDC2 | HF60 | Hybrid | 1 | 294 | 34.6 | $26,000 | **$30,000** | $34,000 |
| 6 | 1130 | HDC2 | AF80 | All-Flash | 0 | – | 184 | $55,000 | **$65,000** | $79,000 |
| 7 | 1813 | HDC2 | AF40 | All-Flash | 0 | – | 46.1 | $9,000 | **$12,000** | $14,000 |
| 8 | 1843 | HDC2 | HF60 | Hybrid | 1 | 168 | 32.6 | $19,000 | **$23,000** | $27,000 |
| 9 | 8863 | HDC2 | HF60 | Hybrid | 0 | 126 | 17.3 | $15,000 | **$18,000** | $21,000 |
| | | | | | | | **Total** | **$245,000** | **$283,825** | **$324,000** |

## Market anchors used
- **HF40** 126TB HDD + 11.52TB SSD refurb — **$16,875** (Enterasource) — *exact match to array #1*
- **HF60** 210TB HDD + 23.04TB cache used — **$23,995** (eBay)
- **AF60** 184TB (48×3.84TB SSD) used — **$34,950** (eBay) — *matches arrays #3/#4*
- **AF80** 184TB used — **$79,500 or best offer** (eBay)
- **AF40** 46TB (24×1.92TB SSD) new — **$19,995** (eBay); used ≈ 55–65% of new
- **AF40/60/80** 92TB flash field-upgrade refurb — **~€53,550** (it-market.com)

Sources: [Enterasource](https://enterasource.com/storage/hpe-nimble) · [ALTA Technologies](https://altatechnologies.com/collections/hpe-nimble-storage) · [Spectra](https://www.spectra.com/hp/used-systems/83/Used-HP-Nimble-Storage.htm) · [eBay HF60](https://www.ebay.com/itm/176841322075) · [eBay AF60](https://www.ebay.com/itm/326495257900) · [eBay AF80](https://www.ebay.com/itm/166495997287) · [eBay AF40](https://www.ebay.com/itm/155085093828) · [it-market AF40](https://it-market.com/en/components/controller-cards/hpe/af40)

## Disclaimer
Figures are good-faith estimates for planning only — not offers or formal appraisals. The used-storage market moves quickly; confirm with a formal quote from a licensed reseller before any transaction.
