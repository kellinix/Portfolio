SELECT 
    "group",
    COUNT(*) AS total_users
FROM ab_test
GROUP BY "group";
