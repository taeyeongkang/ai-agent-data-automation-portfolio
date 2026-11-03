SELECT 
    k_symbol AS 자동이체유형,
    SUM(amount) AS 금액합계,
    ROUND(
        (SUM(amount) / (SELECT SUM(amount) FROM orders)) * 100, 
        2
    ) AS 비중
FROM 
    orders
GROUP BY 
    k_symbol
ORDER BY 
    비중 DESC;
