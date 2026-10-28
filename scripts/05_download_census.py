import os
import json
import urllib.request
import pandas as pd
import duckdb

OUT = "data/raw/census_income_zcta.csv"
CLEAN = "data/processed/noise_residential_clean.parquet"

# api key
# key is read from terminal session so it never ends up in the file or on GitHub
KEY = os.environ.get("CENSUS_API_KEY")
if not KEY:
    raise SystemExit('No API key found. Run: export CENSUS_API_KEY="your-key"')

# download
def fetch(year):
    """Ask the Census API for median household income (B19013) for every ZCTA."""
    url = (f"https://api.census.gov/data/{year}/acs/acs5"
           f"?get=NAME,B19013_001E,B19013_001M&for=zip%20code%20tabulation%20area:*&key={KEY}")
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read().decode("utf-8", errors="replace")
            print(f"{year}: HTTP {r.status}, {len(body):,} characters received")
    except Exception as e:
        print(f"{year}: request failed: {e}")
        return None
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        print(f"{year}: reply was not JSON. First 300 characters:\n{body[:300]}\n")
        return None

# Try the 2020-2024 release first, then fall back to 2019-2023
rows = None
for year in (2024, 2023):
    rows = fetch(year)
    if rows:
        print(f"Using the ACS 5-year release ending in {year}")
        break
if rows is None:
    raise SystemExit("Could not download from the Census API. See the messages above.")

# tidy up data
df = pd.DataFrame(rows[1:], columns=rows[0])   # first row is the header
df = df.rename(columns={
    "B19013_001E": "median_income",
    "B19013_001M": "margin_of_error",
    "zip code tabulation area": "zip",
})[["zip", "median_income", "margin_of_error"]]

# Values arrive as text. Convert to numbers, and turn the Census's special negative codes into blanks.
for col in ["median_income", "margin_of_error"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df.loc[df[col] < 0, col] = None

df["acs_release_end_year"] = year
df.to_csv(OUT, index=False)
print(f"\nDownloaded {len(df):,} ZCTAs, saved to {OUT}")
print(f"  missing median income: {df['median_income'].isna().sum():,}")
print(f"  top-coded at 250,001 or more: {(df['median_income'] >= 250001).sum():,}")

# check coverage of 311 data
con = duckdb.connect()
zips = con.execute(f"""
    SELECT zip, COUNT(*) AS n_requests
    FROM '{CLEAN}'
    WHERE zip IS NOT NULL AND borough IS NOT NULL
    GROUP BY zip
""").df()

m = zips.merge(df, on="zip", how="left")
has_income = m["median_income"].notna()

print(f"\n311 zip codes (with a borough): {len(m)}")
print(f"  with an income value: {has_income.sum()}")
print(f"  share of requests covered: {m.loc[has_income, 'n_requests'].sum() / m['n_requests'].sum():.1%}")

big_missing = m[~has_income & (m["n_requests"] >= 500)]
print(f"\nZips with 500+ requests but no income value: {len(big_missing)}")
print(big_missing.sort_values("n_requests", ascending=False).head(10).to_string(index=False))

print("\nIncome range among matched zips:")
print(m.loc[has_income, "median_income"].describe().round(0).to_string())