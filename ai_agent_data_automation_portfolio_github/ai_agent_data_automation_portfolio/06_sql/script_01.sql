

WITH CTE_CLIENT AS (
    SELECT client_id,
           birth_number,
           SUBSTR(birth_number, 1, 2) AS yy,
           TO_NUMBER(SUBSTR(birth_number, 3, 2)) AS mm,
           SUBSTR(birth_number, 5, 2) AS dd
    FROM client
)
SELECT client_id AS 고객번호,
       yy ||
       TO_CHAR(
           CASE
               WHEN mm >= 50 THEN mm - 50
               ELSE mm
           END,
           'FM00'
       ) ||
       dd AS 생년월일,
       CASE
           WHEN mm >= 50 THEN '여'
           ELSE '남'
       END AS 성별
FROM CTE_CLIENT;