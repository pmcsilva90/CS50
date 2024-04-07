SELECT
    players.first_name,
    players.last_name,
    salaries.salary,
    performances.HR,
    performances.year
FROM
    players
    JOIN salaries ON players.id = salaries.player_id
    JOIN performances ON players.id = performances.player_id

    group by players.id;


select sum(performances.HR) from performances group by player_id
