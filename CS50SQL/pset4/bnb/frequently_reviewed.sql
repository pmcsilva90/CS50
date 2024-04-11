CREATE VIEW
    frequently_reviewed AS
SELECT
    listings.id,
    listings.property_type,
    listings.host_name,
    COUNT(*) AS reviews
FROM
    listings
    JOIN reviews ON listings.id = reviews.listing_id
GROUP BY
    listing_id
ORDER BY
    reviews DESC,
    listings.property_type,
    listings.host_name
LIMIT
    100;
