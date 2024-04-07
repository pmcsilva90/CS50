SELECT
    players.first_name,
    players.last_name,
    salaries.salary,
    salaries.year AS "salary year",
    performances.year AS "performance year",
    performances."home runs"
FROM
    players
    JOIN salaries ON players.id = salaries.player_id
    JOIN (
        SELECT
            *,
            SUM(HR) AS "home runs"
        FROM
            performances
        GROUP BY
            performances.year
    ) AS performances ON salaries.year = performances.year
ORDER BY
    players.id,
    salaries.year,
    performances.year
LIMIT
    100;
