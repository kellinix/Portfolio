SELECT 
    [group] AS test_group,
    COUNT(*) AS total_users,
    SUM(converted) AS conversions,
    ROUND(AVG(converted), 4) AS conversion_rate
FROM ab_test
GROUP BY [group];
