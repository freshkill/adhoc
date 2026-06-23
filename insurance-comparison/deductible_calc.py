#!/usr/bin/env python3
"""
Insurance deductible scenario calculator.

Compares the total multi-year cost of two homeowners-insurance setups
(e.g. a low deductible with higher premium vs. a high deductible you
self-insure against), given an assumed claim pattern.

Usage:
    python3 deductible_calc.py                 # interactive prompts
    python3 deductible_calc.py --demo          # run the worked example
    import deductible_calc; deductible_calc.compare(...)   # as a library
"""

import argparse


def scenario(name, annual_premium, dwelling, deductible_pct,
             claim_amount, num_claims, years):
    """Compute total out-of-pocket for one scenario over `years`."""
    deductible = dwelling * deductible_pct / 100.0
    premium_total = annual_premium * years

    # Per claim: you pay min(claim, deductible). Insurance pays the rest.
    # If claim <= deductible, insurance pays 0 and you pay the whole claim.
    your_cost_per_claim = min(claim_amount, deductible)
    insurer_pays_per_claim = max(0.0, claim_amount - deductible)

    claims_out_of_pocket = your_cost_per_claim * num_claims
    insurer_paid = insurer_pays_per_claim * num_claims
    total = premium_total + claims_out_of_pocket

    return {
        "name": name,
        "annual_premium": annual_premium,
        "deductible_pct": deductible_pct,
        "deductible": deductible,
        "premium_total": premium_total,
        "claim_amount": claim_amount,
        "num_claims": num_claims,
        "your_cost_per_claim": your_cost_per_claim,
        "insurer_pays_per_claim": insurer_pays_per_claim,
        "claims_out_of_pocket": claims_out_of_pocket,
        "insurer_paid": insurer_paid,
        "total": total,
    }


def compare(dwelling, claim_amount, num_claims, years,
            premium_a, deductible_pct_a, name_a,
            premium_b, deductible_pct_b, name_b):
    a = scenario(name_a, premium_a, dwelling, deductible_pct_a,
                 claim_amount, num_claims, years)
    b = scenario(name_b, premium_b, dwelling, deductible_pct_b,
                 claim_amount, num_claims, years)

    def money(x):
        return f"${x:,.0f}"

    print()
    print(f"=== {years}-year comparison "
          f"(dwelling {money(dwelling)}, "
          f"{num_claims} claim(s) of {money(claim_amount)} each) ===")
    print()
    rows = [
        ("Scenario", a["name"], b["name"]),
        ("Annual premium", money(a["annual_premium"]), money(b["annual_premium"])),
        ("Deductible", f"{a['deductible_pct']}%  ({money(a['deductible'])})",
                       f"{b['deductible_pct']}%  ({money(b['deductible'])})"),
        (f"Premium x {years} yrs", money(a["premium_total"]), money(b["premium_total"])),
        ("You pay per claim", money(a["your_cost_per_claim"]), money(b["your_cost_per_claim"])),
        ("Insurer pays per claim", money(a["insurer_pays_per_claim"]), money(b["insurer_pays_per_claim"])),
        ("Claims out-of-pocket", money(a["claims_out_of_pocket"]), money(b["claims_out_of_pocket"])),
        ("TOTAL OUT-OF-POCKET", money(a["total"]), money(b["total"])),
    ]
    w0 = max(len(r[0]) for r in rows)
    w1 = max(len(str(r[1])) for r in rows)
    w2 = max(len(str(r[2])) for r in rows)
    for label, va, vb in rows:
        print(f"{label:<{w0}}  |  {str(va):<{w1}}  |  {str(vb):<{w2}}")

    print()
    diff = a["total"] - b["total"]
    if diff > 0:
        print(f">> {b['name']} is cheaper by {money(diff)} over {years} years.")
    elif diff < 0:
        print(f">> {a['name']} is cheaper by {money(-diff)} over {years} years.")
    else:
        print(">> Both scenarios cost the same.")

    # Break-even: how many claims to justify the pricier-premium scenario?
    extra_premium = a["premium_total"] - b["premium_total"]
    savings_per_claim = b["your_cost_per_claim"] - a["your_cost_per_claim"]
    if extra_premium > 0 and savings_per_claim > 0:
        be = extra_premium / savings_per_claim
        print(f">> {a['name']} only pays off at ~{be:.1f}+ such claims "
              f"in {years} years (saves {money(savings_per_claim)} per claim, "
              f"costs {money(extra_premium)} extra in premium).")
    print()


def interactive():
    def ask(prompt, default):
        raw = input(f"{prompt} [{default}]: ").strip()
        return float(raw) if raw else float(default)

    print("Insurance deductible scenario calculator")
    print("(press Enter to accept the default)\n")
    dwelling = ask("Dwelling / Coverage A value", 404000)
    claim = ask("Claim amount per event", 14000)
    nclaims = int(ask("Number of claims over the period", 1))
    years = int(ask("Years to model", 10))
    print("\n-- Scenario A (e.g. lower deductible, higher premium) --")
    pa = ask("  Annual premium", 5000)
    da = ask("  Wind/Hail deductible %", 2)
    print("\n-- Scenario B (e.g. higher deductible, lower premium) --")
    pb = ask("  Annual premium", 2500)
    db = ask("  Wind/Hail deductible %", 5)

    compare(dwelling, claim, nclaims, years,
            pa, da, f"{da:g}% deductible",
            pb, db, f"{db:g}% deductible")


def demo():
    compare(
        dwelling=404000, claim_amount=14000, num_claims=1, years=10,
        premium_a=5000, deductible_pct_a=2, name_a="2% deductible (double premium)",
        premium_b=2500, deductible_pct_b=5, name_b="5% deductible (self-insure)",
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--demo", action="store_true", help="run the worked example")
    args = parser.parse_args()
    if args.demo:
        demo()
    else:
        interactive()
