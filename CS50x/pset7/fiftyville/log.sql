-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Find crime scene description
SELECT * FROM crime_scene_reports WHERE day = 28 AND month = 7 AND year = 2023 AND street = 'Humphrey Street';

-- "Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery."

-- Check bakery security logs of the day of the crime
SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2023;



