import duckdb
PARQUET_PATH = "data/processed/311_2023_2025.parquet"
con = duckdb.connect()

candidates = ["Noise - Residential", "HEAT/HOT WATER", "Illegal Parking"]
in_list = ", ".join(f"'{c}'" for c in candidates)

print(con.execute(f"""
    WITH t AS (
        SELECT 
        "Problem (formerly Complaint Type)" AS problem,
        TRY_STRPTIME("Created Date", '%m/%d/%Y %I:%M:%S %p') AS created, 
        TRY_STRPTIME(NULLIF(TRIM("Closed Date"), ''), '%m/%d/%Y %I:%M:%S %p') AS closed
    FROM '{PARQUET_PATH}'
    WHERE "Problem (formerly Complaint Type)" IN ({in_list})
)
    SELECT problem,
            COUNT(*) AS n,
            ROUND(100.0 * SUM(CASE WHEN closed IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_no_closed_date,
            ROUND(100.0 * SUM(CASE WHEN closed < created THEN 1 ELSE 0 END) / COUNT(*), 2) AS pct_closed_before_created,
            ROUND(MEDIAN(date_diff('minute', created, closed)) / 60.0, 1) AS median_hours,
            ROUND(QUANTILE_CONT(date_diff('minute', created, closed), 0.9) / 60.0, 1) AS p90_hours
    FROM t
    GROUP BY problem
    ORDER BY n DESC
  """).df().to_string())