SELECT
    --performances.h,
    --salaries.salary
    *
FROM
    performances
    JOIN salaries ON performances.player_id = salaries.player_id
    AND performances.year = salaries.year
    order by player_id
LIMIT
    100;
