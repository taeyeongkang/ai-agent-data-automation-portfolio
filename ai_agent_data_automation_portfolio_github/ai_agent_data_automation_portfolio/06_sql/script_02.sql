SELECT d.a3 AS 지역명
, sum(amount) AS 대출급여합계
, to_char(avg(amount), 'FML999,999,999,999.99', 'NLS_CURRENCY = Kc') 대출금액평균
, max(amount) 대출최고금액
, min(amount) 대출최저금액
FROM loan l JOIN account a ON l.account_id = a.account_id
			  		 JOIN district d ON a.district_id = d.district_id
GROUP BY d.a3;