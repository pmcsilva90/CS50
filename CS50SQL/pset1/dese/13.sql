SELECT name, needs_improvement, unsatisfactory, per_pupil_expenditure FROM districts
JOIN staff_evaluations ON districts.id = staff_evaluations.district_id
JOIN expenditures ON districts.id = expenditures.district_id
ORDER BY per_pupil_expenditure;
