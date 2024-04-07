SELECT
    players.first_name,
    players.last_name,
    salaries.salary,
    salaries.year,
    performances."home runs"
FROM
    players
    JOIN salaries ON players.id = salaries.player_id
    JOIN (
        SELECT
            performances.player_id,
            performances.year,
            SUM(HR) AS "home runs"
        FROM
            performances
        GROUP BY
            performances.player_id
    ) AS performances ON salaries.player_id = performances.player_id
ORDER BY
    players.id,
    salaries.year DESC,
    performances."home runs" DESC,
    salaries.salary DESC;

    -- Todd Zeile id = 20728
