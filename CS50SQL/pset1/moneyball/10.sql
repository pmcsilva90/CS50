SELECT
    players.first_name,
    players.last_name,
    salaries.salary,
    salaries.year,
    perform.year,
    perform."home runs"
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
    ) AS perform ON salaries.player_id = perform.player_id
ORDER BY
    players.id,
    salaries.year DESC,
    perform."home runs" DESC,
    salaries.salary DESC;

    -- Todd Zeile id = 20728
