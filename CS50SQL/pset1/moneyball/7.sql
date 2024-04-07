SELECT
    players.first_name,
    players.last_name
FROM
    players
WHERE
    id = (
        SELECT
            player_id
        FROM
            salaries
        WHERE
            salary = (
                SELECT
                    MAX(salary)
                FROM
                    salaries
            )
    )
