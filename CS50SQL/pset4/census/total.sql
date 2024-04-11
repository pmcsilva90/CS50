create view total as
select count(families), count(households), count(population), count(male), count(female) from census;
