import numpy as np
import pandas as pd
import duckdb
import statsmodels.formula.api as smf

CLEAN = "data/processed/noise_residential_clean.parquet"
CENSUS = "data/raw/census_income_zcta.csv"
TOP_CODE = 250001
SAMPLE_ROWS = 200_000      
REF = "C(borough, Treatment('MANHATTAN'))"   

def pct(res, key):
    """Coefficient on a log scale -> % change, with a 95% confidence interval."""
    ci = res.conf_int().loc[key]
    return (np.exp(res.params[key]) - 1) * 100, (np.exp(ci[0]) - 1) * 100, (np.exp(ci[1]) - 1) * 100

summary = []

# Part A: zip level. Does income still matter once borough is included?

print("PART A: zip-level regression of log(median wait)")

for name in ["all", "excl_cb12", "baseline_jun23_may24"]:
    d = pd.read_csv(f"results/zip_income_{name}.csv")
    d = d[d["median_hours"] > 0].copy()
    d["log_median"] = np.log(d["median_hours"])

    m1 = smf.ols("log_median ~ income_10k", d).fit(cov_type="HC3")
    m2 = smf.ols(f"log_median ~ income_10k + {REF}", d).fit(cov_type="HC3")

    print(f"\nScenario: {name} ({len(d)} zips)")
    for label, m in [("Income only", m1), ("Income + borough", m2)]:
        e, lo, hi = pct(m, "income_10k")
        print(f"  {label:<18} per extra $10k: {e:+.1f}% (95% CI {lo:+.1f}% to {hi:+.1f}%), "
              f"p = {m.pvalues['income_10k']:.3g}, adj. R2 = {m.rsquared_adj:.2f}")
        summary.append({"part": "A", "scenario": name, "model": label, "term": "income per $10k",
                        "pct_change": round(e, 1), "ci_low": round(lo, 1), "ci_high": round(hi, 1),
                        "p": m.pvalues["income_10k"], "adj_r2": round(m.rsquared_adj, 3)})


# Part B: request level. Borough gap after controlling for time and income

print(f"PART B: request-level regression of log(wait), sample of {SAMPLE_ROWS:,} requests")

con = duckdb.connect()
r = con.execute(f"""
    SELECT unique_key, zip, borough, community_board, year, month, weekday, hour,
           resolution_hours
    FROM '{CLEAN}'
    WHERE zip IS NOT NULL AND borough IS NOT NULL AND resolution_hours IS NOT NULL
    ORDER BY hash(unique_key)
    LIMIT 200000
""").df()

census = pd.read_csv(CENSUS, dtype={"zip": str})[["zip", "median_income"]]
r = r.merge(census, on="zip", how="inner")
r = r[r["median_income"].notna() & (r["median_income"] < TOP_CODE)].copy()
r["income_10k"] = r["median_income"] / 10000
r["is_cb12"] = (r["community_board"] == "12 BRONX").astype(int)
# +1 minute so that requests closed within the same minute can be logged
r["log_wait"] = np.log(r["resolution_hours"] + 1 / 60)
groups = pd.factorize(r["zip"])[0]     # standard errors clustered by zip, because income is a zip-level value
print(f"Requests used: {len(r):,} from {r['zip'].nunique()} zips")

base = f"log_wait ~ {REF} + income_10k + C(year) + C(month) + C(weekday) + C(hour)"
models = {
    "B1: borough + income + time": base,
    "B2: B1 + Bronx CB 12 indicator": base + " + is_cb12",
}
for label, formula in models.items():
    m = smf.ols(formula, r).fit(cov_type="cluster", cov_kwds={"groups": groups})
    print(f"\n{label}   (R2 = {m.rsquared:.2f})")
    for b in ["BRONX", "BROOKLYN", "QUEENS", "STATEN ISLAND"]:
        key = f"{REF}[T.{b}]"
        e, lo, hi = pct(m, key)
        print(f"  {b:<14} vs Manhattan: {e:+6.1f}% (95% CI {lo:+.1f}% to {hi:+.1f}%), p = {m.pvalues[key]:.3g}")
        summary.append({"part": "B", "scenario": "sample", "model": label, "term": b,
                        "pct_change": round(e, 1), "ci_low": round(lo, 1), "ci_high": round(hi, 1),
                        "p": m.pvalues[key], "adj_r2": round(m.rsquared_adj, 3)})
    extras = ["income_10k"] + (["is_cb12"] if "is_cb12" in formula else [])
    for key in extras:
        e, lo, hi = pct(m, key)
        name = "income per $10k" if key == "income_10k" else "Bronx CB 12"
        print(f"  {name:<14}: {e:+6.1f}% (95% CI {lo:+.1f}% to {hi:+.1f}%), p = {m.pvalues[key]:.3g}")
        summary.append({"part": "B", "scenario": "sample", "model": label, "term": name,
                        "pct_change": round(e, 1), "ci_low": round(lo, 1), "ci_high": round(hi, 1),
                        "p": m.pvalues[key], "adj_r2": round(m.rsquared_adj, 3)})

pd.DataFrame(summary).to_csv("results/regression_summary.csv", index=False)
print("\nSaved results/regression_summary.csv")