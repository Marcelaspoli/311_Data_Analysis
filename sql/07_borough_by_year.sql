-- Sub-question 2: check if the gap between boroughs hold in every year
SELECT borough, year,
       COUNT(*) AS n_requests,
       ROUND(MEDIAN(resolution_hours), 2) AS median_hours,
       ROUND(QUANTILE_CONT(resolution_hours, 0.9), 2) AS p90_hours
FROM cleaned_311
WHERE borough IS NOT NULL
GROUP BY borough, year
ORDER BY year, median_hours DESC;