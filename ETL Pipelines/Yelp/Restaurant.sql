CREATE TABLE Restaurant (
	id VARCHAR(50),
	rname VARCHAR(50),
	is_closed BIT,
	phone VARCHAR(16),
	reviews INT,
	rating FLOAT,
	zipcode VARCHAR(11),
	city VARCHAR(30),
	country VARCHAR(30),
	latitude FLOAT,
	longitude FLOAT,
	currency VARCHAR(10)

)

SELECT * FROM Restaurant