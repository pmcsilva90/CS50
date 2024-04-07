SELECT
    teams.name,
    SUM(H) AS "total hits"
FROM
    teams
    JOIN performances
WHERE
    teams.id = performances.team_id
WHERE
    YEAR = 2001
GROUP BY
    performances.team_id
ORDER BY
    "total hits";
