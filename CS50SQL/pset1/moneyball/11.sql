SELECT
    --performances.h,
    --salaries.salary
    *,
    (salaries.salary / performances.h) AS "dollars per hit"
FROM
    performances
    JOIN salaries ON performances.player_id = salaries.player_id
    AND performances.year = salaries.year
WHERE
    performances.h > 0
ORDER BY
    player_id
LIMIT
    100;
