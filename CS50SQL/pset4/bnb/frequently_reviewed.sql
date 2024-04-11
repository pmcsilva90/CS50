create view frequently_reviewed as
select listings.id, listings.property_type, listings.host_name, count(*) as reviews
from listings
join reviews on listings.id = reviews.listing_id
group by listing_id
order by reviews DESC
limit 100
