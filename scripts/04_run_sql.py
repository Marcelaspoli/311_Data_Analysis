#Python script to run all SQL queries and save results to CSV files

import duckdb
import glob
import os

con = duckdb.connect()

# Cleaned file = cleaned_311 used in SQL queries.
con.execute("""
    CREATE VIEW cleaned_311 AS
    SELECT * FROM 'data/processed/noise_residential_clean.parquet'
""")

for path in sorted(glob.glob("sql/*.sql")):
    name = os.path.splitext(os.path.basename(path))[0]
    with open(path) as f:
        query = f.read()
    df = con.execute(query).df()
    df.to_csv(f"results/{name}.csv", index=False)
    print(f"\n- {name} ({len(df)} rows) -")
    print(df.head(30).to_string())