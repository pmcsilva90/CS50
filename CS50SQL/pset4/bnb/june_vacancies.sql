create view june_vacancies as

select listings.id, listings.property_type, listings.host_name,
count(*)
as days_vacant
from listings
join availabilities on listings.id = avalabilities.listing_id


group by listings.id
