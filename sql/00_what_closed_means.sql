-- Sub-question 4:How are requests being closed? = Interpretation of "resolution time"
SELECT resolution_description, 
        COUNT(*) AS n,
        ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct_of_requests,
        ROUND(MEDIAN(resolution_hours), 2) AS median_hours
FROM cleaned_311
GROUP BY resolution_description
ORDER BY n DESC
LIMIT 15;
