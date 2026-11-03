SELECT 
    CASE 
        WHEN 2000 - (1900 + TO_NUMBER(SUBSTR(c.birth_number, 1, 2))) <= 39 THEN '30대 이하'
        ELSE '40대 이상'
    END AS 연령대,
    COUNT(*) AS 카드발급개수
FROM 
    card cd
JOIN 
    disp d ON cd.disp_id = d.disp_id
JOIN 
    client c ON d.client_id = c.client_id
GROUP BY 
    CASE 
        WHEN 2000 - (1900 + TO_NUMBER(SUBSTR(c.birth_number, 1, 2))) <= 39 THEN '30대 이하'
        ELSE '40대 이상'
    END
ORDER BY 
    연령대 DESC;