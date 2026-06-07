# Bogue Sound Boating Forecast — Standard Output Template

This is the standard plain-text format to generate when producing the
Bogue, NC boating forecast from https://l-36.com/weather.php (Bogue Inlet
marine zone). Output should be a markdown table — no HTML.

Source URL:
https://l-36.com/weather.php?lat=34.68&lon=-77.04&point1=Bogue%2C%20NC&point2=Marine%20Location%20Near%20Bogue%2C%20NC&tide1=Bogue%20Inlet%2C%20North%20Carolina&tide2=Spooner%20Creek%2C%20North%20Carolina&lat_long1=34.68%2C-77.04&radar=MHX&radar2=LTX&station=mhx&ports=8656483&rss=41035&rss2=bftn7&rss3=clkn7&airport=KNJM&geos=east%2Fma&lat_long2=34.68%2C-77.04&yd10=on&zone1=AMZ158&zone2=AMZ100&v=0.50&where=Bogue%2C%20NC

---

## Output format

```
## Bogue Sound Boating Forecast — Bogue, NC
**Issued:** <NWS issue date/time> | **Forecast period:** <date range>
<Active advisories, e.g. ⚠ Small Craft Advisory: ...>

| Day | Overall | Wind (AM) | Wind (PM) | Sound (AM) | Sound (PM) | Tide (high) | Solunar | Best Window | Flags |
|-----|---------|-----------|-----------|------------|------------|-------------|---------|-------------|-------|
| **<Day, Date>** | **<n>/5** | <speed/dir> — <n>/5 (NWS|est.) | ... | ... | ... | <time, height> — <n>/5 | <rating or N/A> | <time range> | <hazards or "none noted"> |

### Tide details (Bogue Inlet)
- **<Day> (NWS|est.):** High <time> (<height>) · Low <time> (<height>) · ...

### Source legend
- **(NWS)** = directly from NWS marine forecast (zone AMZ158/AMZ100) and Bogue Inlet tide tables.
- **(est.)** = projected/estimated — explain method (e.g. tide times advanced ~50 min/day from latest NWS anchor).

### Scoring keys
- **Wind:** <10 kt = 5/5 · 10–15 = 4/5 · 15–20 = 3/5 · 20–25 = 2/5 · >25 or gusts 30+ = 1/5 (gusts pull score down a tier)
- **Sound:** Flat = 5/5 · Light chop = 4/5 · Moderate chop = 3/5 · Choppy = 2/5 · Rough/Very rough = 1/5
- **Tide:** High tide 8 AM–4 PM = 5/5 ideal · just outside window = 4/5 · well outside = 3/5 or lower
- **Overall:** average of Wind/Sound/Tide, capped by active hazards — Small Craft Advisory caps at 2/5, thunderstorm risk caps at 3/5

**Bottom line:** <1-2 sentence summary highlighting the best day and any day to avoid>
```

---

## Generation rules

1. **Fetch fresh data** from the source URL each time — do not reuse stale forecasts.
2. **Sound conditions** must use only the NWS "adjacent sounds and rivers" wording
   (flat / light chop / moderate chop / choppy / rough). Never substitute ocean
   seas (e.g. "3 to 5 ft") for sound ratings — these are separate.
3. **Split AM/PM** for wind and sound whenever the NWS text distinguishes
   morning vs. afternoon conditions (e.g. "becoming E in the afternoon",
   "increasing to a moderate chop in the afternoon"). If the forecast gives
   one rating for the full day, use a single combined cell or repeat the value.
4. **Tides**: use NWS/Bogue Inlet tide table values directly when available
   and tag them `(NWS)`. For days beyond what the source publishes, project
   by advancing each tide ~50 minutes/day from the latest confirmed anchor
   point and tag them `(est.)`.
5. **Solunar/fishing activity**: include if present on the source; otherwise
   mark `N/A`.
6. **Hazard caps**: an active Small Craft Advisory caps a day's overall score
   at 2/5; thunderstorm/lightning risk caps it at 3/5 — regardless of the
   averaged wind/sound/tide score. Always flag these explicitly in the Flags
   column and call them out in the bottom-line summary.
7. **Best day**: mark the day with the highest overall score (and no active
   hazards) with a "⭐ Best Day" annotation in the Day column.
8. **Low-confidence / extended outlook days**: if the source only provides a
   brief multi-day summary (rather than day-by-day detail) for later days,
   group them into a single row, label as "extended outlook (low confidence)",
   and tag wind/sound values `(est.)`.
9. **Bottom line**: always end with a 1–2 sentence summary naming the best
   day and flagging any day to avoid (advisories, storms, rough chop).
