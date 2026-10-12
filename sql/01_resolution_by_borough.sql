-- Sub-question 1 (borough): typical and slow-end resolution times
SELECT borough,
       COUNT(*) AS n_requests,
       ROUND(MEDIAN(resolution_hours), 2) AS median_hours,
       ROUND(QUANTILE_CONT(resolution_hours, 0.9), 2) AS p90_hours
FROM cleaned_311
WHERE borough IS NOT NULL
GROUP BY borough
ORDER BY median_hours DESC;