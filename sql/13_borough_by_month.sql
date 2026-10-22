-- check if the Sep 2024 and Oct 2025 waves hit every borough or only some
SELECT year, month, borough,
       COUNT(*) AS n_requests,
       ROUND(MEDIAN(resolution_hours), 2) AS median_hours
FROM cleaned_311
WHERE borough IS NOT NULL
GROUP BY year, month, borough
ORDER BY year, month, borough;