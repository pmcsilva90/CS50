create view june_vacancies as

select listings.id, listings.property_type, listings.host_name "" as days_vacant
