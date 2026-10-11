-- Group By
--The GROUP BY clause is often used with aggregate functions like COUNT(), MAX(), MIN(), SUM(), AVG() to group the result-set by one or more columns.
SELECT COUNT (CUSTOMER_ID), country
from customers 
group by country;

-- Group by Join 
--SQL statement lists the number of orders made by each customer:
select customers.customer_name, COUNT (orders.order_id)
from orders 
left join customers ON orders.customer_id = customers.customer_id 
group by customer_name;

-- HAVING Clause 
/* the having clause was added to SQL because WHERE clause cannot be used with aggregate functions. 
Aggregate functions are often used with GROUP BY clauses, and by adding 
HAVING we can write conditions like we do with WHERE clauses. */

-- List only countris that are represented more than 5 times. 
select count(customer_id), country
from customers
group by country
having count (customer_id) > 5;

-- More  having examples 
-- the following SQL statement lists only orders with a total price of 400$ OR MORE:
SELECT order_details.order_id, SUM (products.price)
FROM order_details 
LEFT JOIN products ON  order_details.product_id = products.product_id
GROUP BY order_id
HAVING SUM (products.price) > 400.00;

--CASE 
/* The CASE expression goes through conditions and returns a value when the first condition
is met (like an if-then-else statement).
Once a condition is true, it will stop reading and return the result. 
If no conditions are true, it returns the value in the ELSE clause.
If there is no ELSE part and no conditions are true, it returns NULL. */
select product_name, 
CASE 
	WHEN price < 10 THEN 'Low price product'
	WHEN price > 50 THEN 'High price product'
ELSE 
	'Normal product '
END 
FROM products;

-- with aliases 
-- when a column name is not specified for the 'case' field, the parser uses case as the column name. 
-- to specify a column name, add an alias after the END keyword. 
select product_name,
CASE 
	WHEN price < 10 THEN 'Low price product'
	WHEN price > 50 THEN 'High price product'
ELSE 
	'Normal product'
END as "price category"
from products;

--EXISTS 
-- The exists operator is used to test for the exitstence of any record in a sub query. 
-- the exists operator returns TRUE if the sub query returens one or more records. 
-- Return all customers that is represented in the orders table. 
SELECT customers.customer_name
FROM customers 
WHERE EXISTS (
select order_id
from orders 
where customer_id = customers.customer_id);

--NOT EXISTS 
--to check which customers that do not have any ordrs, we can use the NOT operator together with 
--the EXISTS operator;
--Return all customers is NOT represented in the orders table:

SELECT customers.customer_name
from customers
WHERE NOT EXISTS (SELECT order_id 
from orders 
where customers.customer_id = customers.customer_id);

--ANY 
/* the ANY operator allows you to perform a comparison between a single column value and a range of other values:
the any operator:
	* returns boolean value as result 
	* returns TRUE if ANY of the sub query values meet the condition
ANY means that the condition will be true if the operation is true for any of he values in the range. 
*/
-- List product that have any records in the order_details table with a quantity larger than 120.

SELECT product_name
FROM products
WHERE product_id = ANY ( 
SELECT product_id
FROM order_details
WHERE quantity > 120);


