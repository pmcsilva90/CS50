create view frequently_reviewed as
select listings.id, listings.property_type, listings.host_name,

select listing_id, count(*) from reviews group by listing_id

limit 100
