USE Practice
/* Q1. Write a query to create a duplicate table with and without data present? */
-- Query to create duplicate table with data
SELECT * INTO EmployeeCopy FROM [MeetConciergeDb3].[dbo].Employee

-- Query to create duplicate table without data
SELECT * INTO EmployeeStructure FROM [MeetConciergeDb3].[dbo].Employee
WHERE 1=2;

-- Process to create duplicate table by maintaining architecture
/*
Step 1: Right Click on Table --> Script Table as --> Create to --> New Query Editor Window
Step 2: Replace all the "original table name fields" with "duplicate table name" 
Step 3: Execute
*/

-- To copy data from one table to other
INSERT INTO [Practice].[dbo].EmployeeInfo (empName, empEmail, empPassword, empRoleId, empCmpId) 
SELECT M.empName, M.empEmail, M.empPassword, M.empRoleId, M.empCmpId 
FROM [MeetConciergeDb3].[dbo].Employee AS M
WHERE 1=1;