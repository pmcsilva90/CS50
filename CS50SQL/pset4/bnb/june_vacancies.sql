create view june_vacancies as

select listings.id, listings.property_type, listings.host_name, days_vacant
from listings
join (select listing_id, count(*) as days_vacant from availabilities where date between '2023-06-01' and '2023-06-30' and available = 'TRUE' group by listing_id order by listing_id) as availabilities
on listings.id = avalabilities.listing_id


