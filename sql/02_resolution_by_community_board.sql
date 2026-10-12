-- Sub-question 1 (neighborhood): only boards with enough requests are kept for reliable medians
SELECT community_board,
       borough,
       COUNT(*) AS n_requests,
       ROUND(MEDIAN(resolution_hours), 2) AS median_hours,
       ROUND(QUANTILE_CONT(resolution_hours, 0.9), 2) AS p90_hours
FROM cleaned_311
WHERE borough IS NOT NULL
  AND community_board NOT LIKE 'Unspecified%'
  AND community_board LIKE '%' || borough 
GROUP BY community_board, borough
HAVING COUNT(*) >= 500
ORDER BY median_hours DESC;