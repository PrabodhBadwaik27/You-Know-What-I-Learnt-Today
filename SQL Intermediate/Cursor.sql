SELECT * FROM Sales.SalesPerson

DECLARE distributed_commission CURSOR FOR
	SELECT BusinessEntityID, Bonus, CommissionPct
	FROM Sales.SalesPerson
	ORDER BY Bonus DESC

OPEN distributed_commission;

DECLARE @id INT; 
DECLARE @bonus FLOAT;
DECLARE @commission FLOAT;

FETCH NEXT FROM distributed_commission INTO @id, @bonus, @commission;

WHILE @@FETCH_STATUS = 0
	BEGIN 
		PRINT CONCAT(@id, ' - ', @bonus*@commission)
		FETCH NEXT FROM distributed_commission INTO @id, @bonus, @commission
	END;

CLOSE distributed_commission;
DEALLOCATE distributed_commission;

	 
		
