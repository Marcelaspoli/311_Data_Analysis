-- Sub-question 3: trends over time
SELECT year, month,
       COUNT(*) AS n_requests,
       ROUND(MEDIAN(resolution_hours), 2) AS median_hours,
       ROUND(QUANTILE_CONT(resolution_hours, 0.9), 2) AS p90_hours
FROM cleaned_311
GROUP BY year, month
ORDER BY year, month;