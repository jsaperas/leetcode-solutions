/* Write your PL/SQL query statement below */
SELECT 
    MAX(CASE WHEN SalaryRank = 2 THEN salary ELSE NULL END) AS SecondHighestSalary
FROM (
    SELECT 
        salary,
        RANK() OVER (ORDER BY salary DESC) AS SalaryRank
    FROM Employee
)