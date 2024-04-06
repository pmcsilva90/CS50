SELECT
    name,
    per_pupil_expenditure,
    graduated
FROM
    schools
    JOIN graduation_rates ON schools.id = graduation_rates.school_id
    JOIN expenditures ON graduation_rates.school_id = expenditures.id
ORDER BY
    per_pupil_expenditure DESC,
    name;
