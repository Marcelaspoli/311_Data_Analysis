-- Check if "no evidence" rises as wait time increases 
SELECT CASE
           WHEN resolution_hours < 0.5 THEN '1. under 30 min'
           WHEN resolution_hours < 1 THEN '2. 30-60 min'
           WHEN resolution_hours < 2 THEN '3. 1-2 h'
           WHEN resolution_hours < 4 THEN '4. 2-4 h'
           ELSE '5. over 4 h'
       END AS wait_bucket,
       COUNT(*) AS n,
       ROUND(100.0 * SUM(CASE WHEN resolution_description LIKE '%no evidence%' THEN 1 ELSE 0 END)
             / COUNT(*), 1) AS pct_no_evidence,
       ROUND(100.0 * SUM(CASE WHEN resolution_description LIKE '%took action to fix%' THEN 1 ELSE 0 END)
             / COUNT(*), 1) AS pct_action_taken
FROM cleaned_311
GROUP BY wait_bucket
ORDER BY wait_bucket;