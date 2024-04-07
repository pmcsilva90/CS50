SELECT
    players.first_name,
    players.last_name,
    (salaries.salary / performances.h) AS "dollars per hit"
    -- performances.h,
    -- salaries.salary,
    -- salaries.year as s_year,
    -- performances.year as p_year
FROM
    players
    JOIN performances ON players.id = performances.player_id
    JOIN salaries ON performances.player_id = salaries.player_id
    AND performances.year = salaries.year
WHERE
    performances.h > 0
    AND salaries.year = 2001
ORDER BY
    "dollars per hit",
    players.first_name,
    players.last_name
LIMIT
    10;
