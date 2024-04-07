select avg(salary) as "average salary" from salaries group by team_id order by "average salary" limit 10;
