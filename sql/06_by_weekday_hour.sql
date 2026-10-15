-- Sub-question 3: weekday and time the of day patterns (based on when the complaint was created)
SELECT isodow(created) AS weekday_num,   -- 1 = Monday ... 7 = Sunday
       weekday,
       hour,
       COUNT(*) AS n_requests,
       ROUND(MEDIAN(resolution_hours), 2) AS median_hours
FROM cleaned_311
GROUP BY weekday_num, weekday, hour
ORDER BY weekday_num, hour;