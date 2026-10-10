import duckdb

PARQUET_PATH = "data/processed/311_2023_2025.parquet"
con = duckdb.connect()

print("Top 20 complaint types:")
print(con.execute(f"""
    SELECT "Problem (formerly Complaint Type)" AS problem,
           Agency,
           COUNT(*) AS n
    FROM '{PARQUET_PATH}'
    GROUP BY 1, 2
    ORDER BY n DESC
    LIMIT 20
""").df().to_string())

print("\nSample date values (to check the format):")
print(con.execute(f"""
    SELECT "Created Date", "Closed Date"
    FROM '{PARQUET_PATH}'
    LIMIT 5
""").df().to_string())

print("\nStatus counts:")
print(con.execute(f"""
    SELECT Status, COUNT(*) AS n
    FROM '{PARQUET_PATH}'
    GROUP BY 1 ORDER BY n DESC
""").df().to_string())
