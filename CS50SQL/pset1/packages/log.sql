
-- *** The Lost Letter ***

sqlite> SELECT * FROM addresses WHERE address = "2 Finnegan Street"; -- this query yields no match


-- Find the sender's address in the address table
sqlite> SELECT * FROM addresses WHERE address = "900 Somerville Avenue";

-- Find packages sent from sender's address
sqlite> SELECT * FROM packages WHERE from_address_id = (
   ...> SELECT id FROM addresses WHERE address = "900 Somerville Avenue");






-- *** The Devious Delivery ***

-- *** The Forgotten Gift ***

