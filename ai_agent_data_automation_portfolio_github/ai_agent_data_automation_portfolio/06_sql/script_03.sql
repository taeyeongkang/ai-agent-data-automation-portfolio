SELECT c.client_id AS 고객번호,
       TO_CHAR(TO_DATE(t.trans_date, 'YYMMDD'), 'MM') AS 거래월,
       SUM(t.amount) AS 거래금액합계,
       MAX(t.amount) AS 최고거래금액
FROM client c
JOIN disp d
    ON c.client_id = d.client_id
JOIN account a
    ON d.account_id = a.account_id
JOIN trans t
    ON a.account_id = t.account_id
GROUP BY c.client_id,
         TO_CHAR(TO_DATE(t.trans_date, 'YYMMDD'), 'MM')
ORDER BY 고객번호, 거래월;