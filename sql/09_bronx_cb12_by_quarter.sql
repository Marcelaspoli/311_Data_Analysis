-- Check if Bronx Community Board 12 is behind the Bronx volume surge and when did it start
SELECT year,
       quarter(created) AS quarter,
       CASE WHEN community_board = '12 BRONX' THEN 'Bronx CB 12' ELSE 'Rest of Bronx' END AS area,
       COUNT(*) AS n_requests,
       ROUND(MEDIAN(resolution_hours), 2) AS median_hours,
       ROUND(QUANTILE_CONT(resolution_hours, 0.9), 2) AS p90_hours
FROM cleaned_311
WHERE borough = 'BRONX'
GROUP BY year, quarter, area
ORDER BY year, quarter, area;