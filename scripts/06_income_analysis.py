import os
import numpy as np
import pandas as pd
import duckdb
from scipy import stats

CLEAN = "data/processed/noise_residential_clean.parquet"
CENSUS = "data/raw/census_income_zcta.csv"
MIN_REQUESTS = 300     # zips with fewer requests give unreliable medians
TOP_CODE = 250001      # Census ceiling: true income is higher but unknown, drop these

# Each scenario is a filter on the 311 requests
SCENARIOS = {
    "all": "TRUE",
    "excl_cb12": "community_board <> '12 BRONX'",
    "baseline_jun23_may24": "created >= DATE '2023-06-01' AND created < DATE '2024-06-01'",
}

os.makedirs("results", exist_ok=True)
con = duckdb.connect()
con.execute(f"CREATE VIEW cleaned_311 AS SELECT * FROM '{CLEAN}'")
census = pd.read_csv(CENSUS, dtype={"zip": str})   # keep zips as text

summary = []
for name, where in SCENARIOS.items():
    print("\n")
    print(f"SCENARIO: {name}")
    print("\n")

    # 1. one row per zip, median and p90 resolution time
    zdf = con.execute(f"""
        SELECT zip,
               MODE(borough) AS borough,
               COUNT(*) AS n_requests,
               MEDIAN(resolution_hours) AS median_hours,
               QUANTILE_CONT(resolution_hours, 0.9) AS p90_hours
        FROM cleaned_311
        WHERE zip IS NOT NULL AND borough IS NOT NULL AND {where}
        GROUP BY zip
        HAVING COUNT(*) >= {MIN_REQUESTS}
    """).df()

    # 2. add income, drop zips with no income or a capped income
    z = zdf.merge(census[["zip", "median_income"]], on="zip", how="left")
    n_enough = len(z)
    z = z[z["median_income"].notna() & (z["median_income"] < TOP_CODE)].copy()
    print(f"Zips with {MIN_REQUESTS}+ requests: {n_enough}; used after dropping "
          f"missing or capped income: {len(z)}")
    z["income_10k"] = z["median_income"] / 10000
    z.round(2).to_csv(f"results/zip_income_{name}.csv", index=False)   # small file for Tableau

    # 3. is income associated with response time?
    rho, p = stats.spearmanr(z["median_income"], z["median_hours"])
    # Simple regression: log(median hours) against income in $10,000 steps.
    lr = stats.linregress(z["income_10k"], np.log(z["median_hours"]))
    pct_per_10k = (np.exp(lr.slope) - 1) * 100
    print(f"\nSpearman correlation (income vs median hours): {rho:.2f} (p = {p:.3g})")
    print(f"Each extra $10,000 of median income goes with a {pct_per_10k:+.1f}% change "
          f"in a zip's median wait (p = {lr.pvalue:.3g}, R-squared = {lr.rvalue**2:.2f})")

    # 4. same test inside each borough, so borough differences don't drive the result 
    print("\nWithin each borough (Spearman):")
    within = {}
    for b, g in z.groupby("borough"):
        if len(g) >= 8:
            r, pb = stats.spearmanr(g["median_income"], g["median_hours"])
            within[b] = r
            print(f"  {b:<14} zips = {len(g):>3}   rho = {r:+.2f}   p = {pb:.3g}")
        else:
            print(f"  {b:<14} zips = {len(g):>3}   too few zips to test")

    # 5. income quartiles measured across individual requests 
    z["income_quartile"] = pd.qcut(
        z["median_income"], 4,
        labels=["Q1 (lowest income)", "Q2", "Q3", "Q4 (highest income)"]
    ).astype(str)
    con.register(f"zq_{name}", z[["zip", "income_quartile"]])
    q = con.execute(f"""
        SELECT q.income_quartile,
               COUNT(DISTINCT c.zip) AS zips,
               COUNT(*) AS requests,
               ROUND(MEDIAN(c.resolution_hours), 2) AS median_hours,
               ROUND(QUANTILE_CONT(c.resolution_hours, 0.9), 2) AS p90_hours
        FROM cleaned_311 c
        JOIN zq_{name} q ON c.zip = q.zip
        WHERE {where}
        GROUP BY q.income_quartile
        ORDER BY q.income_quartile
    """).df()
    ranges = z.groupby("income_quartile")["median_income"].agg(["min", "max"]).round(0)
    q = q.merge(ranges, left_on="income_quartile", right_index=True)
    print("\nBy zip income quartile:")
    print(q.rename(columns={"min": "income_min", "max": "income_max"}).to_string(index=False))

    summary.append({
        "scenario": name, "zips_used": len(z),
        "spearman_rho": round(rho, 3), "spearman_p": p,
        "pct_change_per_10k": round(pct_per_10k, 1), "regression_p": lr.pvalue,
        "r_squared": round(lr.rvalue ** 2, 3),
        **{f"rho_{b}": round(r, 3) for b, r in within.items()},
    })

pd.DataFrame(summary).to_csv("results/income_association_summary.csv", index=False)
print("\nSaved results/income_association_summary.csv and results/zip_income_*.csv")