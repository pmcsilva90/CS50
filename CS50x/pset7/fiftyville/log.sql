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

-- Given that earliest departure from Fiftyville on 2023-07-29 has the destination airport id of 4, find details of airport with id 4.
SELECT * FROM airports WHERE id = 4;
-- Results in LaGuardia Airport in New York City






