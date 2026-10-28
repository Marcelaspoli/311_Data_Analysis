-- sub question 3: weekday pattern
SELECT isodow(created) AS weekday_num,
       weekday,
       COUNT(*) AS n_requests,
       ROUND(MEDIAN(resolution_hours), 2) AS median_hours,
       ROUND(QUANTILE_CONT(resolution_hours, 0.9), 2) AS p90_hours
FROM cleaned_311
GROUP BY weekday_num, weekday
ORDER BY weekday_num;