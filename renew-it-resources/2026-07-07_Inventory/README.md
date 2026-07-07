# Renew IT Resources — HPE Nimble Inventory & Reseller-Direct Valuation

**Inventory date:** 2026-07-07
**Prepared for:** justalink357@gmail.com
**Scenario:** Direct wholesale sale to a reseller/ITAD firm, with **certified data destruction (NIST 800-88 wipe, drives retained) included** as part of the service.

## Contents
| File | Description |
|------|-------------|
| `HPE_Nimble_Asset_Inventory.xlsx` | Original asset inventory (as supplied) — 9 HPE Nimble arrays |
| `HPE_Nimble_Used_Price_Estimate_2026-07-07.xlsx` | Reseller-direct offer + retail-resale reference + sources/methodology |
| `README.md` | This summary |

## The deal being modeled
Selling **direct to a reseller** (not to an end user), so you accept a wholesale price cut in exchange for speed and certainty. The reseller performs **certified data sanitization to NIST 800-88 "Purge"** (crypto-erase/secure-erase) with a **Certificate of Destruction**; drives are wiped and **retained** in the arrays (not physically shredded), so the flash/HDD value is preserved.

**Net Offer = (Retail resale value × reseller wholesale factor ~50%) − certified data-wipe allowance.**

> All nine arrays carry HW End-of-Support **7/31/2028** — still HPE-supportable, which keeps reseller buy prices up.

## Estimated reseller-direct offer

| # | S/N | Model | HDD (TB) | SSD (TB) | Retail (ref) | Gross @50% | Wipe | Net Low | **Net Point** | Net High |
|---|-----|-------|--------:|--------:|----:|----:|----:|----:|-------:|----:|
| 1 | 0862 | HF40 | 126 | 11.52 | $16,875 | $8,400 | $216 | $6,900 | **$8,200** | $9,600 |
| 2 | 4469 | AF60 | – | 253 | $47,000 | $23,500 | $384 | $19,400 | **$23,100** | $26,900 |
| 3 | 7343 | AF60 | – | 184 | $37,000 | $18,500 | $384 | $15,200 | **$18,100** | $21,100 |
| 4 | 8949 | AF60 | – | 184 | $34,950 | $17,500 | $192 | $14,500 | **$17,300** | $20,100 |
| 5 | 4349 | HF60 | 294 | 34.6 | $30,000 | $15,000 | $384 | $12,200 | **$14,600** | $17,000 |
| 6 | 1130 | AF80 | – | 184 | $65,000 | $32,500 | $192 | $27,100 | **$32,300** | $37,500 |
| 7 | 1813 | AF40 | – | 46.1 | $12,000 | $6,000 | $192 | $4,900 | **$5,800** | $6,800 |
| 8 | 1843 | HF60 | 168 | 32.6 | $23,000 | $11,500 | $384 | $9,300 | **$11,100** | $13,000 |
| 9 | 8863 | HF60 | 126 | 17.3 | $18,000 | $9,000 | $240 | $7,300 | **$8,800** | $10,200 |
| | | | | **Total** | **$283,825** | **$142,000** | **$2,568** | **$116,700** | **$139,300** | **$162,200** |

**Bottom line:** roughly a **$139K point offer** (range **~$117K–$162K**) selling direct to a reseller with the wipe included — versus ~$284K if the individual arrays were sold at retail secondary-market prices. The ~50% haircut is the reseller's margin for refurb, warranty, holding, and resale risk; the certified data-wipe adds only ~$2.6K across the fleet.

## Market anchors (retail resale basis)
- **HF40** 126TB + 11.52TB SSD refurb — **$16,875** (Enterasource) — *exact match to array #1*
- **HF60** 210TB + 23.04TB cache used — **$23,995** (eBay)
- **AF60** 184TB (48×3.84TB SSD) used — **$34,950** (eBay) — *matches arrays #3/#4*
- **AF80** 184TB used — **$79,500 or best offer** (eBay)
- **AF40** 46TB (24×1.92TB SSD) new — **$19,995** (eBay); used ≈ 55–65% of new

Sources: [Enterasource](https://enterasource.com/storage/hpe-nimble) · [ALTA Technologies](https://altatechnologies.com/collections/hpe-nimble-storage) · [Spectra](https://www.spectra.com/hp/used-systems/83/Used-HP-Nimble-Storage.htm) · [eBay HF60](https://www.ebay.com/itm/176841322075) · [eBay AF60](https://www.ebay.com/itm/326495257900) · [eBay AF80](https://www.ebay.com/itm/166495997287) · [eBay AF40](https://www.ebay.com/itm/155085093828) · [it-market AF40](https://it-market.com/en/components/controller-cards/hpe/af40)

## Negotiation notes
- Get the **wipe / Certificate of Destruction stated in writing as included at no charge** — some resellers net it out of the offer (as modeled here).
- Ask the reseller to **itemize wipe cost vs. hardware value** so you see the true hardware offer.
- Estimated drive counts are approximate (drive sizes weren't in the source inventory); the wipe fee is immaterial to the total either way.
- The **50% wholesale factor** is the biggest lever — for still-supported all-flash (AF60/AF80) you can reasonably push toward the high end (~55–58%).

## Disclaimer
Good-faith planning estimates only — not offers or formal appraisals. The used-storage market moves quickly; confirm with written quotes from licensed resellers before transacting.
