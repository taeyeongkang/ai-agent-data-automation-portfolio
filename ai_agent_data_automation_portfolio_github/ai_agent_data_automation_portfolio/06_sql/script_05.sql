SELECT 
    대출상환상태,
    ROUND(AVG(잔액), 2) AS 평균잔액,
    ROUND(AVG(거래빈도), 2) AS 평균거래빈도
FROM (
    SELECT 
        c.client_id AS 고객번호,
        AVG(t.amount) AS 평균거래금액,
        COUNT(t.trans_id) AS 거래빈도,
        AVG(t.amount) AS 잔액, 
        l.status AS 대출상환상태
    FROM loan l
    JOIN account a ON l.account_id = a.account_id
    JOIN disp d    ON a.account_id = d.account_id
    JOIN client c  ON d.client_id = c.client_id
    JOIN trans t   ON a.account_id = t.account_id
    GROUP BY c.client_id, l.status
) SUB
GROUP BY 
    대출상환상태;
