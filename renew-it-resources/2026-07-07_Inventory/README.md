# Renew IT Resources — HPE Nimble Inventory & Used-Value Estimate

**Inventory date:** 2026-07-07
**Prepared for:** justalink357@gmail.com

## Contents
| File | Description |
|------|-------------|
| `HPE_Nimble_Asset_Inventory.csv` | Asset inventory — 9 HPE Nimble arrays, with hardware config (CPU, memory, drives) and for-sale asking prices |
| `HPE_InfoSight_Arrays_01232026.csv` | Source HPE InfoSight export (serials, raw capacity, ports, support status) |
| `Prospective_Buyers.csv` | 5 companies to approach for a direct sale with certified data destruction |
| `HPE_Nimble_Used_Price_Estimate_2026-07-07__Used_Price_Estimate.csv` | Retail secondary-market value estimates (reference basis) |
| `HPE_Nimble_Used_Price_Estimate_2026-07-07__Sources_Methodology.csv` | Sources & methodology notes |
| `README.md` | This summary |

> Spreadsheets are stored as CSV so they render as tables directly on GitHub. Open `../../csv-viewer.html` (e.g. via GitHub Pages) for an in-browser viewer/editor.

## For-sale asking prices (reduced 60% for quick reseller-direct sale)
Asking prices were cut **60% below retail secondary-market value** to price for a fast direct sale to a reseller, with the expectation that the buyer provides **certified data destruction (NIST 800-88 wipe + Certificate of Destruction)** as part of the deal.

| # | S/N | Model | Type | CPU | Cores | Memory | Drives | Retail est. | **Asking** |
|---|-----|-------|------|-----|------:|-------:|--------|----:|-------:|
| 1 | 0862 | HF40 | Hybrid | Xeon Silver | 12 | 128 GB | 10TB HDD / 3TB SSD cache | $16,875 | **$6,750** |
| 2 | 4469 | AF60 | All-Flash | Xeon Silver | 16 | 256 GB | 3.84TB SSD | $47,000 | **$18,800** |
| 3 | 7343 | AF60 | All-Flash | Xeon Silver | 16 | 256 GB | 3.84TB SSD | $37,000 | **$14,800** |
| 4 | 8949 | AF60 | All-Flash | Xeon Silver | 16 | 256 GB | 3.84TB SSD | $34,950 | **$13,980** |
| 5 | 4349 | HF60 | Hybrid | Xeon Silver | 16 | 192 GB | 12TB HDD / 3TB SSD cache | $30,000 | **$12,000** |
| 6 | 1130 | AF80 | All-Flash | Xeon Gold | 20 | 384 GB | 3.84TB SSD | $65,000 | **$26,000** |
| 7 | 1813 | AF40 | All-Flash | Xeon Silver | 12 | 192 GB | 1.92TB SSD | $12,000 | **$4,800** |
| 8 | 1843 | HF60 | Hybrid | Xeon Silver | 16 | 192 GB | 12TB HDD / 3TB SSD cache | $23,000 | **$9,200** |
| 9 | 8863 | HF60 | Hybrid | Xeon Silver | 16 | 192 GB | 10TB HDD / 3TB SSD cache | $18,000 | **$7,200** |
| | | | | | | | **Total** | **$283,825** | **$113,530** |

All memory is DDR4 ECC (2666 MT/s on hybrid HF models, 2933 MT/s on all-flash AF models). Full detail — including host interfaces, raw HDD/SSD TB, and HW EOS dates — is in `HPE_Nimble_Asset_Inventory.csv`.

> All nine arrays carry a HW End-of-Support date of **7/31/2028** — still HPE-supportable, which sustains resale demand today.

## Where to sell — 5 prospective buyers (see `Prospective_Buyers.csv`)
All buy used HPE Nimble AF/HF arrays for cash or trade-in; ask each for a written quote **with certified NIST 800-88 data destruction + Certificate included**.
1. **ITAMG** — enterprise-storage buyback; **R2v3 + NAID AAA certified data destruction** (best fit); free quote ~48h — (212) 651-8500
2. **ALTA Technologies** — largest US used-Nimble inventory; cash or trade-in — (952) 934-4443
3. **Spectra** — buys/sells used Nimble since 1982 — (714) 970-7000
4. **Enterasource** — refurb Nimble reseller, buys trade-ins — (302) 526-9203
5. **Core 4 Solutions** — high-volume AF60/AF80/HF60 buyer/seller — (952) 548-5720

> Send all five the same package at once and let them compete — expect a 20–40% spread between low and high bid.

## Retail market anchors (basis for the retail estimates)
- **HF40** 126TB HDD + 11.52TB SSD refurb — **$16,875** (Enterasource) — *exact match to array #1*
- **HF60** 210TB HDD + 23.04TB cache used — **$23,995** (eBay)
- **AF60** 184TB (48×3.84TB SSD) used — **$34,950** (eBay) — *matches arrays #3/#4*
- **AF80** 184TB used — **$79,500 or best offer** (eBay)
- **AF40** 46TB (24×1.92TB SSD) new — **$19,995** (eBay); used ≈ 55–65% of new
- **AF40/60/80** 92TB flash field-upgrade refurb — **~€53,550** (it-market.com)

Sources: [Enterasource](https://enterasource.com/storage/hpe-nimble) · [ALTA Technologies](https://altatechnologies.com/collections/hpe-nimble-storage) · [Spectra](https://www.spectra.com/hp/used-systems/83/Used-HP-Nimble-Storage.htm) · [eBay HF60](https://www.ebay.com/itm/176841322075) · [eBay AF60](https://www.ebay.com/itm/326495257900) · [eBay AF80](https://www.ebay.com/itm/166495997287) · [eBay AF40](https://www.ebay.com/itm/155085093828) · [it-market AF40](https://it-market.com/en/components/controller-cards/hpe/af40)

## Disclaimer
Figures are good-faith estimates for planning only — not offers or formal appraisals. The used-storage market moves quickly; confirm with a formal quote from a licensed reseller before any transaction.
