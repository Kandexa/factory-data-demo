-- Daily Summary (basic)

-- 1) Stop events today
SELECT machine_id, COUNT(*) AS stop_events_today
FROM machine_events
WHERE state='stop' AND ts::date=CURRENT_DATE
GROUP BY machine_id
ORDER BY stop_events_today DESC;

-- 2) Faults last hour
SELECT machine_id, COUNT(*) AS faults_last_hour
FROM machine_events
WHERE state='fault' AND ts >= NOW() - INTERVAL '1 hour'
GROUP BY machine_id
ORDER BY faults_last_hour DESC;

-- 3) Production today
SELECT machine_id,
       SUM(good_count) AS good,
       SUM(scrap_count) AS scrap,
       SUM(good_count + scrap_count) AS total
FROM production
WHERE ts::date=CURRENT_DATE
GROUP BY machine_id
ORDER BY total DESC;
