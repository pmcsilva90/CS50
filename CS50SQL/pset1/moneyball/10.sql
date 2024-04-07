select players.first_name, players.last_name, salaries.salary, performances.HR, performances.year from

players join salaries on players.id = salaries.player_id
join performances on players.id = performances.player_id


