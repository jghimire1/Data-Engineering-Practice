-- specify column name to select the data 
SELECT customer_name, country FROM customers; 

-- select distinct data 
SELECT DISTINCT country FROM customers; 

--get the count of the countries from the customer table 
SELECT COUNT(DISTINCT country) FROM customers; 

/* Filter Records
●	The WHERE clause is used to filter records.
●	It is used to extract only those records that fulfil a specified condition.
●	If we want to return only the records where city is London, we can specify that in the WHERE clause: */ 

SELECT * FROM customers
WHERE city = 'London';

-- sort data, ●	The ORDER BY keyword sorts the records in ascending order by default. To sort the records in descending order, use the DESC keyword. 
SELECT * FROM products ORDER BY price;

SELECT * FROM products
ORDER BY price DESC;

--The limit clause 
SELECT * FROM customers
LIMIT 20;

/*The OFFSET Clause
●	The OFFSET clause is used to specify where to start selecting the records to return.
●	If you want to return 20 records, but start at number 40, you can use both LIMIT and OFFSET.
●	Note: The first record is number 0, so when you specify OFFSET 40 it means starting at record number 41.
●	Return 20 records, starting from the 41th record: */

SELECT * FROM customers
LIMIT 20 OFFSET 40;

-- Min - the MIN() function returns the smallest value of the selected column.
SELECT MIN(price)
FROM products;

-- Max - The MAX() function returns the largest value of the selected column.
SELECT MAX(price)
FROM products;

--set column name 
SELECT MIN(price) AS lowest_price
FROM products;

-- count , The COUNT() function returns the number of rows that matches a specified criterion. If the specified criterion is a column name, the COUNT() function returns the number of columns with that name.
SELECT COUNT(customer_id)
FROM customers;

SELECT COUNT(customer_id)
FROM customers
WHERE city = 'London';

-- SUM - The SUM() function returns the total sum of a numeric column. 
SELECT SUM(quantity)
FROM order_details;

--AVG - The AVG() function returns the average value of a numeric column.
SELECT AVG(price)
FROM products;

-- With decimals 

SELECT AVG(price)::NUMERIC(10,2)
FROM products;





