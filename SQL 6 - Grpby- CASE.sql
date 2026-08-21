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

