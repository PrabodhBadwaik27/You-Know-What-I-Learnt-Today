------------------------------------------------------------
--Checklist
--1. INNER JOIN
--2. OUTER JOIN
--3. CROSS APPLY
--4. OUTER APPLY
------------------------------------------------------------
USE Practice
SELECT M.Id, M.Name, D.Period, D.Quantity
FROM TblMaster AS M
INNER JOIN TblDetails AS D
ON M.Id = D.Id
--1.
--2.
ORDER BY D.Quantity 
--3.
DESC

USE Practice

SELECT M.Id, M.Name, D.Period, D.Quantity
FROM TblMaster AS M
FULL OUTER JOIN TblDetails AS D
ON M.Id = D.Id
--1.
--2.
ORDER BY CAST(D.Period AS DATE) 
--3.
DESC

USE Practice
SELECT M.Id, M.Name, D.Period, D.Quantity
FROM TblMaster AS M
INNER JOIN (
	SELECT TOP 2 D.Id, D.Period, D.Quantity
	FROM TblDetails AS D 
	--1.
	--2. 
	ORDER BY D.Quantity 
	--3.
	DESC
) AS D
ON M.Id = D.Id

USE Practice
SELECT M.Id, M.Name, D.Period, D.Quantity
FROM TblMaster AS M
CROSS APPLY (
	SELECT TOP 2 D.Id, D.Period, D.Quantity
	FROM TblDetails AS D
	WHERE M.Id = D.Id
	ORDER BY CAST(D.Period AS DATE) DESC 
) AS D

USE Practice
SELECT M.Id, M.Name, D.Period, D.Quantity
FROM TblMaster AS M
OUTER APPLY (
	SELECT TOP 2 D.Id, D.Period, D.Quantity
	FROM TblDetails AS D
	WHERE M.Id = D.Id
	ORDER BY CAST(D.Period AS DATE) DESC 
) AS D
