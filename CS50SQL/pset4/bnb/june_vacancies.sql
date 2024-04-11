CREATE VIEW
    june_vacancies AS
SELECT
    listings.id,
    listings.property_type,
    listings.host_name,
    days_vacant
FROM
    listings
JOIN (
    SELECT
        listing_id,
        count(*) AS days_vacant
    FROM
        availabilities
    WHERE
        "date" BETWEEN '2023-06-01' AND '2023-06-30'
    AND
        available = 'TRUE'
    GROUP BY listing_id
    ORDER BY listing_id
    )
AS june ON listings.id = june.listing_id;
