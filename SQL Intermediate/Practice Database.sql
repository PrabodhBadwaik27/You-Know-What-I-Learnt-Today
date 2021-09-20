USE Practice
Create Table TblMaster (
Id int PRIMARY KEY IDENTITY,
Name varchar(10)
)

USE Practice
Create Table TblDetails (
Id int,
Period date,
Quantity int
)

USE Practice
Insert Into TblMaster(Name) 
Values ('A'), ('B'), ('C'), ('D');

Use Practice
Insert Into TblDetails(Id, Period, Quantity)
Values (1, '2021-12-12', 10),
(1, '2021-11-11', 20),
(1, '2021-10-10', 30),
(2, '2021-9-9', 40),
(2, '2021-8-8', 30),
(3, '2021-7-7', 40); 
--------------------------------------------------------
USE Practice
SELECT * FROM TblMaster
SELECT * FROM TblDetails
--------------------------------------------------------
USE Practice
CREATE TABLE Products (
	product_id INT PRIMARY KEY IDENTITY,
	product_name VARCHAR(20),
	brand_id INT,
	category_id INT,
	model_year INT,
	list_price FLOAT
)

CREATE TABLE Categories (
	category_id INT PRIMARY KEY IDENTITY,
	category_name VARCHAR(20)
)

USE Practice
INSERT INTO Categories (category_name)
VALUES ('Children Bicycles'), ('Comfort Bicycles'), ('Cruisers Bicycles'), 
('Cyclocross Bicycles'), ('Electric Bicycles'), ('Electric Bikes');

USE Practice
ALTER TABLE Products
ADD CONSTRAINT FK_Products_Categories 
FOREIGN KEY(category_id)
REFERENCES Categories(category_id)

USE Practice
SELECT * FROM Categories
SELECT * FROM Products