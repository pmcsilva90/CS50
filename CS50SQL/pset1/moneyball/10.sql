-- sqlite> select *, sum(performances.HR) from performances group by player_id order by player_id limit 100;
SELECT
    players.first_name,
    players.last_name,
    salaries.salary,
    salaries.year
FROM
    players
    JOIN salaries ON players.id = salaries.player_id
    limit 100;


