SELECT
    *
FROM
    salaries
    JOIN performances ON salaries.player_id = performances.player_id
ORDER BY
    
    salaries.year,
    performances.year
LIMIT
    100;
