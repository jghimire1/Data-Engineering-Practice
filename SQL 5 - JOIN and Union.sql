-- JOIN 
-- Types 
	/* ●	INNER JOIN: Returns records that have matching values in both tables
●	LEFT JOIN: Returns all records from the left table, and the matched records from the right table. The result is 0 records from the right side if there is no match. 
●	RIGHT JOIN: Returns all records from the right table, and the matched records from the left table
●	FULL JOIN: Returns all records when there is a match in either left or right table
*/ 

-- Inner join 
select * from testproducts;
select * from categories;
-- Joining testproducts to categories using the category_id column:
select testproduct_id, product_name, category_name from testproducts 
inner join categories ON testproducts.category_id = categories.category_id; 

--Left Join 
-- join testproducts to categories using the category-id column:
SELECT testproduct_id, product_name, category_name
from testproducts
LEFT JOIN categories ON testproducts.category_id = categories.category_id; 

--Right join
-- The RIGHT JOIN keyword selects ALL records from the "right" table, and the matching records from the "left" table. The result is 0 records from the left side if there is no match.
-- join testproducts to categories using the category-id column:
select testproduct_id, product_name, category_name
from testproducts 
RIGHT JOIN categories ON testproducts.category_id = categories.category_id; 

--Full join 
/*●	The FULL JOIN keyword selects ALL records from both tables, even if there is not a match. For rows with a match the values from both tables are available, 
if there is not a match the empty fields will get the value NULL.
●	By using FULL JOIN we will get all records from both the categories table and the testproducts table:
For example: Join testproducts to categories using the category_id column:
*/
select testproduct_id, product_name, category_name
from testproducts
FULL JOIN categories ON testproducts.category_id = categories.category_id; 

-- cross join 
/* ●	The CROSS JOIN keyword matches ALL records from the "left" table with EACH record from the "right" table.
●	That means that all records from the "right" table will be returned for each record in the "left" table.
●	This way of joining can potentially return very large table, and you should not use it if you do not have to.
●	for example: Join testproducts to categories using the CROSS JOIN keyword:
*/ 
select testproduct_id, product_name, category_name
from testproducts
CROSS JOIN categories;

--UNION 
/* 
The UNION operator is used to combine the result-set of two or more queries.
The queries in the union must follow these rules:
●	They must have the same number of columns
●	The columns must have the same data types
●	The columns must be in the same order
*/
-- EXAMPLE: COMBINE products and test products 
select product_id, product_name
from products
union 
select testproduct_id, product_name
from testproducts
order by product_id; 

-- Union vs UNION ALL 
/* ●	With the UNION operator, if some rows in the two queries returns the exact same result, only one row will be listed, because UNION selects only distinct values.
●	Use UNION ALL to return duplicate values.
●	Let's make some changes to the queries, so that we have duplicate values in the result:*/

--Union all 

SELECT product_id
FROM products
UNION ALL
SELECT testproduct_id
FROM testproducts
ORDER BY product_id;


-- union 

SELECT product_id
FROM products
UNION 
SELECT testproduct_id
FROM testproducts
ORDER BY product_id;







