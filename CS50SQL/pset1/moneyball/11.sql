SELECT
    players.first_name,
    players.last_name,
    salaries.salary,
    salaries.year,
    performances.year,
    performances.HR
FROM
    players
    JOIN salaries ON players.id = salaries.player_id
    
ORDER BY
    players.id,
    salaries.year DESC,
    performances.HR DESC,
    salaries.salary DESC;

    -- Todd Zeile id = 20728
