-- public school districts with above-average per-pupil expenditures

SELECT * FROM districts JOIN expenditures ON districts.id = expenditures.district_id WHERE type = "Public School District" AND per_pupil_expenditure >
(SELECT AVG(per_pupil_expenditure) FROM expenditures);

SELECT * FROM districts JOIN expenditures ON districts.id = expenditures.district_id JOIN staff_evaluations ON districts.id = staff_evaluations.district_id WHERE type = "Public School District" AND per_pupil_expenditure >
(SELECT AVG(per_pupil_expenditure) FROM expenditures);

