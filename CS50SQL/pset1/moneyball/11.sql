SELECT
    *
FROM
    salaries
    JOIN performances ON salaries.player_id = performances.player_id
ORDER BY
    player_id,
    salaries.year,
    performances.year
LIMIT
    100;
