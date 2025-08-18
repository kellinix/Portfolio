SELECT 
    [group] AS test_group,
    DATE(timestamp) AS test_date,
    COUNT(*) AS total_users,
    SUM(converted) AS conversions,
    ROUND(AVG(converted), 4) AS conversion_rate
FROM ab_test
GROUP BY [group], DATE(timestamp)
ORDER BY test_date, test_group;
