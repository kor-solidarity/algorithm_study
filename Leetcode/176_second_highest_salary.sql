-- https://leetcode.com/problems/second-highest-salary/
-- Runtime: 288 ms, faster than 15.65% of MySQL online submissions for Second Highest Salary.

-- CREATE TABLE EMPLOYEE
-- (
--     ID     INT PRIMARY KEY,
--     SALARY INT
-- );

-- INSERT INTO EMPLOYEE
-- VALUES (1, 100);
-- INSERT INTO EMPLOYEE
-- VALUES (2, 100);

SELECT (SELECT DISTINCT SALARY FROM EMPLOYEE ORDER BY SALARY DESC LIMIT 1, 1) AS SECONDHIGHESTSALARY;

