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
# Convert the date columns to timestamp format, create nulls for invalid entries, rename columns, trim zip codes.

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

# Step 2 = Count the number of problematic entries before removals. 
# Numbers go into log so the cleaning is documented.

step("1. Noise - Residential rows", count())
step("   duplicate unique keys",
     con.execute("SELECT COUNT(*) - COUNT(DISTINCT unique_key) FROM noise").fetchone()[0])
step("   created date failed to parse", count("created IS NULL"))
step("   no closed date (kept, flagged as open)", count("closed IS NULL"))
step("   closed before created (removed)", count("closed < created"))
step(f"   closed after more than {MAX_HOURS} hours (removed)",
     count(f"date_diff('minute', created, closed) > {MAX_HOURS * 60}"))
step("   borough missing or unspecified", count("borough IS NULL"))
step("   zip missing or invalid", count("zip IS NULL"))


# Step 3 = Build the clean table 
# Remove clearly broken rows and add columns for analysis

con.execute(f"""
CREATE TABLE clean AS
SELECT *,
       closed IS NULL AS is_open,

       date_diff('minute', created, closed) / 60.0 AS resolution_hours,

       year(created) AS year,
       month(created) AS month,
       dayname(created) AS weekday,
       hour(created) AS hour
FROM noise
WHERE created IS NOT NULL          
  AND (closed IS NULL              
       OR (closed >= created       
           AND date_diff('minute', created, closed) <= {MAX_HOURS * 60}))  
""")

step("2. Rows after cleaning", con.execute("SELECT COUNT(*) FROM clean").fetchone()[0])

# Step 4 = Save the cleaned data and the log of what was removed.

con.execute(f"COPY clean TO '{OUT}' (FORMAT PARQUET)")   
pd.DataFrame(log).to_csv(LOG, index=False)               
print(f"\nSaved {OUT} and {LOG}")



