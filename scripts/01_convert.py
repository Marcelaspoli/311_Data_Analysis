import duckdb

CSV_PATH = "data/raw/311_subset.csv"
PARQUET_PATH = "data/processed/311_2023_2025.parquet"

con = duckdb.connect()
con.execute("SET memory_limit='4GB'")

con.execute(f"""
    COPY (
        SELECT * FROM read_csv('{CSV_PATH}', all_varchar=true)
    ) TO '{PARQUET_PATH}' (FORMAT PARQUET)
""")

total = con.execute(f"SELECT COUNT(*) FROM '{PARQUET_PATH}'").fetchone()[0]
print(f"Rows in Parquet file: {total:,}")

print("\nColumns:")
print(con.execute(f"DESCRIBE SELECT * FROM '{PARQUET_PATH}'").df()[["column_name"]])
