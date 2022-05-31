-- https://leetcode.com/problems/combine-two-tables/
-- Runtime: 340 ms, faster than 58.12% of MySQL online submissions for Combine Two Tables.

-- create table Address
-- (
-- 	AddressId int
-- 		constraint Address_pk
-- 			primary key,
-- 	PersonId int,
-- 	City varchar,
-- 	State varchar
-- );
--
-- create table Person
-- (
-- 	personId int
-- 		constraint table_name_pk
-- 			primary key,
-- 	FirstName varchar,
-- 	LastName int
-- );

SELECT FIRSTNAME, LASTNAME, CITY, STATE
FROM PERSON P LEFT JOIN  ADDRESS A  ON A.PERSONID = P.PERSONID;

