SELECT
    *
FROM
    salaries
WHERE
    salaries.player_id = (
        SELECT
            performances.player_id
        FROM
            performances
        WHERE
            performances.HR = (
                SELECT
                    MAX(performances.HR)
                FROM
                    performances
                WHERE
                    performances.year = 2001
            )
    )
    AND salaries.year = 2001;
