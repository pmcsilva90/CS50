

SELECT
    players.first_name,
    players.last_name,
    (salaries.salary / performances.h) AS "dollars per hit"
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



SELECT
    players.first_name,
    players.last_name,
    (salaries.salary / performances.RBI) AS "dollars per RBI"
FROM
    players
    JOIN performances ON players.id = performances.player_id
    JOIN salaries ON performances.player_id = salaries.player_id
    AND performances.year = salaries.year
WHERE
    performances.RBI > 0
    AND salaries.year = 2001
ORDER BY
    "dollars per RBI",
    players.first_name,
    players.last_name
LIMIT
    10;
