
-- *** The Lost Letter ***

-- Find the receiver's address in the addresses table
SELECT * FROM addresses WHERE address = "2 Finnegan Street"; -- this query yields no match


-- Find the sender's address in the address table
SELECT * FROM addresses WHERE address = "900 Somerville Avenue";

-- Find packages sent from sender's address
SELECT * FROM packages WHERE from_address_id = (
SELECT id FROM addresses WHERE address = "900 Somerville Avenue");

-- Given one of the packges contents has the description "Congratulatory letter", it can be assumed to be the lost letter. The query shows it was sent to address ID 854

-- Find the address with ID of 854
SELECT * FROM addresses WHERE id = 854;
-- Query returns address 2 Finnigan Street, which is one character different from Anneke's spelling.


-- *** The Devious Delivery ***

-- Find a package where there is no address from the sender
SELECT * FROM packages WHERE from_address_id IS NULL;
-- Returns ID: 5098, contents: Duck Debugger, to address ID: 50

-- Find ID of address where the package was dropped
SELECT * FROM scans WHERE package_id = (
    SELECT id FROM packages WHERE from_address_id IS NULL)
AND action = 'Drop';

-- Find the corresponding address of that ID
SELECT * FROM addresses WHERE id = (
    SELECT address_id FROM scans WHERE package_id = (
        SELECT id FROM packages WHERE from_address_id IS NULL)
    AND action = 'Drop');
-- Query returns 7 Humboldt Place, a Police Station


-- *** The Forgotten Gift ***

-- Gather information about the mentioned addresses
sqlite> SELECT * FROM addresses WHERE address = '728 Maple Place' OR address = '109 Tileston Street';

-- Find more about the package
sqlite> SELECT * FROM packages WHERE from_address_id = (
   ...> SELECT id FROM addresses WHERE address = '728 Maple Place');
-- Contents are chalk and was delivered to address with ID 4425, which doesn't match with the ID of address 109 Tileston Street

-- Find what address that ID corresponds to
sqlite> SELECT * FROM addresses WHERE id = (
   ...> SELECT to_address_id FROM packages WHERE from_address_id = (
   ...> SELECT id FROM addresses WHERE address = '728 Maple Place'));
-- Query returns 8681 Beacon Street, a business address




-- 728 Maple Place ID 4983
