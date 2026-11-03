WITH Monthly_Balance AS (
    SELECT 
        account_id AS 계좌번호,
        SUBSTR(trans_date, 1, 4) AS 구분연월, 
        AVG(amount) AS 월평균잔액
    FROM trans
    WHERE trans_date LIKE '93%' 
    GROUP BY account_id, SUBSTR(trans_date, 1, 4)
),
Lagged_Data AS (
    SELECT 
        계좌번호,
        구분연월,
        월평균잔액 AS m0,
        LAG(월평균잔액, 1) OVER (PARTITION BY 계좌번호 ORDER BY 구분연월) AS m1,
        LAG(월평균잔액, 2) OVER (PARTITION BY 계좌번호 ORDER BY 구분연월) AS m2,
        LAG(월평균잔액, 3) OVER (PARTITION BY 계좌번호 ORDER BY 구분연월) AS m3,
        LAG(월평균잔액, 4) OVER (PARTITION BY 계좌번호 ORDER BY 구분연월) AS m4,
        LAG(월평균잔액, 5) OVER (PARTITION BY 계좌번호 ORDER BY 구분연월) AS m5  
    FROM Monthly_Balance
)
SELECT 
    l.account_id AS 계좌번호,
    d.구분연월 AS 구분연월,
    l.amount AS 대출잔액,
    ROUND((d.m0 + NVL(d.m1,0) + NVL(d.m2,0)) / 3, 2) AS "3개월평균잔액",
    CASE 
        WHEN ((d.m0 + NVL(d.m1,0) + NVL(d.m2,0)) / 3) <= ((NVL(d.m3,0) + NVL(d.m4,0) + NVL(d.m5,0)) / 3) * 0.5 THEN 'Y'
        ELSE 'N'
    END AS 연체위험여부
FROM loan l
JOIN Lagged_Data d ON l.account_id = d.계좌번호
WHERE d.구분연월 = '9307';