-- Sub-questions 1 and 4. The same outcome appears under several wordings, needs to be grouped.
SELECT borough,
       outcome,
       COUNT(*) AS n,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY borough), 1) AS pct_within_borough
FROM (
    SELECT borough,
           CASE
               WHEN resolution_description LIKE '%took action to fix%' THEN 'Action taken'
               WHEN resolution_description LIKE '%no evidence%' THEN 'No evidence of violation'
               WHEN resolution_description LIKE '%action was not necessary%'
                 OR resolution_description LIKE '%no criminal violation existed%' THEN 'No action necessary'
               WHEN resolution_description LIKE '%unable to gain entry%' THEN 'Unable to gain entry'
               WHEN resolution_description LIKE '%were gone%' THEN 'Gone on arrival'
               ELSE 'Other'
           END AS outcome
    FROM cleaned_311
    WHERE borough IS NOT NULL
) t
GROUP BY borough, outcome
ORDER BY borough, n DESC;