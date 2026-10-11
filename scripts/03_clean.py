import duckdb
import pandas as pd
import os

SRC = "data/processed/311_2023_2025.parquet"            
OUT = "data/processed/noise_residential_clean.parquet"  # cleaned output
LOG = "results/cleaning_log.csv"                        # small log of what was removed
MAX_HOURS = 24 * 30 # closure time bigger than 30 days is considered an outlier and removed

os.makedirs("results", exist_ok=True)
con = duckdb.connect()
log = [] 

def step(label, n):
    """Print a row count and store it in the cleaning log."""
    log.append({"step": label, "rows": int(n)})
    print(f"{label}: {n:,}")

# Step 1 = Build a working table containing only the selected column "Noise - Residential",
# convert the date columns to timestamp format, create nulls for invalid entries, rename columns, trim zip codes.
con.execute(f"""
CREATE TABLE noise AS
SELECT
    "Unique Key" AS unique_key,

    TRY_STRPTIME("Created Date", '%m/%d/%Y %I:%M:%S %p') AS created,
    TRY_STRPTIME(NULLIF(TRIM("Closed Date"), ''), '%m/%d/%Y %I:%M:%S %p') AS closed,

    Agency AS agency,
    "Problem (formerly Complaint Type)" AS problem,
    "Problem Detail (formerly Descriptor)" AS problem_detail,
    Status AS status,
    "Resolution Description" AS resolution_description,
    "Community Board" AS community_board,

    CASE WHEN UPPER(TRIM(Borough)) IN ('', 'UNSPECIFIED') THEN NULL
         ELSE UPPER(TRIM(Borough)) END AS borough,

    CASE WHEN regexp_matches(TRIM("Incident Zip"), '^[0-9]{{5}}')
         THEN LEFT(TRIM("Incident Zip"), 5) END AS zip
FROM '{SRC}'
WHERE "Problem (formerly Complaint Type)" = 'Noise - Residential'
""")

def count(where="TRUE"):
    """Count rows in the working table that match a condition."""
    return con.execute(f"SELECT COUNT(*) FROM noise WHERE {where}").fetchone()[0]

# Step 2. Count the number of problematic entries before removals. 
# Numbers go into log so the cleaning is documented.

#Step 3. Build the clean table: remove clearly broken rows and add columns for analysis



