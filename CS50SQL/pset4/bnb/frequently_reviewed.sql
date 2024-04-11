create view frequently_reviewed as
select listings.id, listings.property_type, listings.host_name,

select listing_id, count(*) as reviews from reviews group by listing_id
order by reviews DESC
limit 100
