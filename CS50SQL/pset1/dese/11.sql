SELECT
    name,
    per_pupil_expenditure,
    graduated
FROM
    schools
    JOIN graduation_rates ON schools.id = graduation_rates.school_id
    JOIN expenditures ON schools.id = expenditures.id
ORDER BY
    per_pupil_expenditure DESC,
    name;
