-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find crime scene description.
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7 AND year = 2023 AND street = 'Humphrey Street';

-- "Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery."

-- Find mentions of 'bakery' in interviews.
SELECT * FROM interviews WHERE transcript LIKE '%bakery%';

-- Given this description from an Ruth's interview:
-- "Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame."
-- Check bakery security logs of the day of the crime between 10:15am and 10:25am
SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2023 AND hour = 10 AND minute BETWEEN 15 and 25;

-- Given this description from Eugene's interview:
-- "I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money."
-- Find withdrawal transactions on 2023-07-28 on Leggett Street.
SELECT * FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2023 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street';

-- Checking the above table against the bank accounts table, the thief must have one of the id's on this table:
SELECT * FROM bank_accounts WHERE account_number IN (
SELECT account_number FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2023 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street');

-- Given this description from Raymond's interview:
-- "As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket."
-- Find phone calls on 2023-07-28 of a duration of less than 60 seconds.
SELECT * FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60;

-- Find earliest flight departing from Fiftyville on 2023-07-29.
SELECT * FROM (
    SELECT * FROM airports
    JOIN flights ON airports.id = flights.origin_airport_id)
WHERE year = 2023 AND month = 7 AND day = 29
ORDER BY hour, minute;

-- Given that earliest departure from Fiftyville on 2023-07-29 has the destination airport id of 4 and flight id of 36, find details of airport with id 4.
SELECT * FROM airports WHERE id = 4;
-- Results in LaGuardia Airport in New York City

-- Thief is must be among this list of passengers on flight with id of 36.
SELECT * FROM passengers WHERE flight_id = 36;

-- With all the information gathered above, I will try to find the thief using this query:
-- From the people table, find an ID's that are in the bank accounts table that also are in the transactions table where a withdrawal transaction was made on 2023-07-28 on Leggett Street
SELECT * FROM people WHERE
    id IN (
        SELECT person_id FROM bank_accounts WHERE account_number IN (
            SELECT account_number FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2023 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street'))
-- and the person's phone number is the list of callers on the same date in which the duration was less than 60 seconds
AND phone_number IN (
    SELECT caller FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60)
-- and the person's passport number was in the list of passports in with flight ID 36 which was the earliest departure from Fiftyville the day after the crime
AND passport_number IN (
    SELECT passport_number FROM passengers WHERE flight_id = 36)
-- and the person's licence plate was among the bakery security logs on the date of the crime within 10 minutes of the crime
AND license_plate IN (
    SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2023 AND hour = 10 AND minute BETWEEN 15 and 25);

-- The query returns only one result with whose name is Bruce, phone number is (367) 555-5533, passport number is 5773159633 and license plate is 94KL13X

-- I can now try to find the thief's accomplice by finding the receiver's number when the thief made the phone call on the day of the crime
SELECT * FROM phone_calls WHERE caller = '(367) 555-5533' AND year = 2023 AND month = 7 AND day = 28 AND duration < 60;
-- The query returns one result where the receiver's phone number is (375) 555-8161






