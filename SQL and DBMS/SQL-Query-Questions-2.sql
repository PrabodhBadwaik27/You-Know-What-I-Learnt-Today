/* Write a query to fetch all the records from the EmployeeInfo table ordered by EmpLname in descending order and Department in the ascending order */
USE Practice
SELECT * FROM EmployeeBg
ORDER BY EmpLname DESC, Department ASC;

/* Write a query to fetch details of all employees excluding the employees with first names, “Sanjay” and “Sonia” from the EmployeeInfo table */
USE Practice
SELECT * FROM EmployeeBg
WHERE EmpFname NOT IN ('Sanjay', 'Sonia');

/* Write a query to fetch all employees who hold the managerial position. */ 
USE Practice
SELECT * FROM EmployeeBg AS B
INNER JOIN EmployeeAc AS A
ON B.EmpId = A.EmpID
WHERE A.EmpPosition = 'Manager';

/* Write a query to fetch the department-wise count of employees sorted by department’s count in ascending order */
USE Practice
SELECT Department, Count(*) AS EmpDeptCount 
FROM EmployeeBg 
GROUP BY Department
ORDER BY EmpDeptCount ASC;

/* Write a query to calculate the even and odd records from a table */
USE Practice
SELECT *
FROM (SELECT *, ROW_NUMBER() OVER(ORDER BY EmpId) AS rownum 
		FROM EmployeeBg) T
WHERE T.rownum%2=0;  

USE Practice
SELECT *
FROM (SELECT *, ROW_NUMBER() OVER(ORDER BY EmpId) AS rownum 
		FROM EmployeeBg) T
WHERE T.rownum%2!=0;

/* Write a SQL query to retrieve employee details from EmployeeInfo table who have a date of joining in the EmployeePosition table */
USE Practice
SELECT * FROM EmployeeBg B
WHERE EXISTS (SELECT  * 
				FROM EmployeeAc A
				WHERE A.EmpID = B.EmpId);

/* Write a query to retrieve two minimum and maximum salaries from the EmployeePosition table */
USE Practice
SELECT TOP 2 *
FROM EmployeeBg AS B
INNER JOIN EmployeeAc AS A
ON A.EmpID=B.EmpId
ORDER BY A.SALARY 
ASC 
--DESC

/* Write a query to find the Nth highest salary from the table without using TOP/limit keyword */
WITH Result AS (
	SELECT Salary, DENSE_RANK() OVER(ORDER BY Salary DESC) AS denserank
	FROM EmployeeAc
)
SELECT Salary 
FROM Result
WHERE denserank=5

/* Write a query to retrieve duplicate records from a table */
USE Practice
SELECT EmpFname, EmpLname, Department, Count(*) 
FROM EmployeeBg  
GROUP BY EmpFname, EmpLname, Department
HAVING COUNT(*) > 1;

 /* Write a query to retrieve the list of employees working in the same department */
USE Practice
SELECT Department, EmpID, EmpFname, EmpLname
FROM EmployeeBg
GROUP BY Department, EmpID, EmpFname, EmpLname
ORDER BY Department, EmpID, EmpFname, EmpLname

/* Write a query to retrieve the last 3 records from the EmployeeInfo table */
USE Practice
SELECT TOP 3 * 
FROM EmployeeBg
ORDER BY EmpId DESC

/* Write a query to find the third-highest salary from the EmpPosition table */
SELECT TOP 1 A.SALARY AS ThirdHighest
FROM (SELECT TOP 3 SALARY
		FROM EmployeeAc 
		ORDER BY SALARY DESC) A
ORDER BY A.SALARY ASC

/* Write a query to retrieve Departments who have greater than 2 employees working in it */
SELECT A.Department
FROM (SELECT Department 
		FROM EmployeeBg
		GROUP BY Department 
		HAVING COUNT(EmpId)>=2) A
 
 /* Write a query to fetch 50% records from the EmployeeInfo table */
 SELECT TOP 50 PERCENT *
 FROM EmployeeBg

/* 
Rank Functions 
ROW_NUMBER - It assigns the sequential rank number to each unique record.
RANK - It assigns the rank number to each row in a partition. It skips the number for similar values.
DENSE_RANK - It assigns the rank number to each row in a partition. It does not skip the number for similar values.
NTILE(N) - It divides the number of rows as per specified partition and assigns unique value in the partition.
*/

/*
Remaining Topics
1. Indexes - Clustered and Non-clustered
2. Views
3. Normalization
*/

-- [Reference](https://www.interviewbit.com/sql-interview-questions/)