USE PRACTICE
SELECT * FROM Products
SELECT * FROM Categories
---------------------------------------------------------------------------------
USE Practice
	SELECT C.category_name AS Category, COUNT(P.product_id) AS Total_Products
	FROM Products AS P
	INNER JOIN Categories AS C
	ON P.category_id = c.category_id
	GROUP BY P.category_id, category_name
---------------------------------------------------------------------------------

SELECT * FROM (
	SELECT category_name, product_id, brand_id
	FROM Products AS P
	INNER JOIN Categories AS C
	ON P.category_id = C.category_id
) AS T
PIVOT (
	COUNT(product_id)
	FOR category_name IN (
		[Children Bicycles], 
		[Comfort Bicycles], 
		[Cruisers Bicycles], 
		[Cyclocross Bicycles],
		[Electric Bicycles], 
		[Electric Bikes]
	)
) AS pivot_table