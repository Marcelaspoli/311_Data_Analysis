import duckdb

PARQUET_PATH = "data/processed/311_2023_2025.parquet"
con = duckdb.connect()

print(con.execute(f"""
    WITH t AS (
        SELECT
            Borough,
            TRY_STRPTIME("Created Date", '%m/%d/%Y %I:%M:%S %p') AS created,
            TRY_STRPTIME(NULLIF(TRIM("Closed Date"), ''), '%m/%d/%Y %I:%M:%S %p') AS closed
        FROM '{PARQUET_PATH}'
        WHERE "Problem (formerly Complaint Type)" = 'Noise - Residential'
    )
    SELECT Borough,
           COUNT(*) AS n,
           ROUND(MEDIAN(date_diff('minute', created, closed)) / 60.0, 2) AS median_hours,
           ROUND(QUANTILE_CONT(date_diff('minute', created, closed), 0.9) / 60.0, 2) AS p90_hours
    FROM t
    WHERE closed >= created
    GROUP BY Borough
    ORDER BY median_hours DESC
""").df().to_string())