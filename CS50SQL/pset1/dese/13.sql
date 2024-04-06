SELECT
    type AS "Type of School District",
    ROUND(AVG(per_pupil_expenditure), 2) AS "Average Per Pupil Expenditure"
FROM
    (
        SELECT
            *
        FROM
            districts
            JOIN expenditures ON districts.id = expenditures.district_id
    )
GROUP BY
    type;
