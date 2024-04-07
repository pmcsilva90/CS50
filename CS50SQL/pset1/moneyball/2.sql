SELECT
    salaries.year,
    salary
FROM
    players
    JOIN salaries ON players.id = salaries.player_id
WHERE
    first_name = 'Cal'
    AND last_name = 'Ripken'
ORDER BY
    salaries.year DESC;
