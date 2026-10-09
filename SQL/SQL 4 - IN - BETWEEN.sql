--SQL 4 - in, between 
-- IN 
SELECT * FROM customers
WHERE country IN ('Germany', 'France', 'UK');

--NOT IN 
SELECT * FROM customers
WHERE country NOT IN ('Germany', 'France', 'UK');

-- IN (SELECT)
SELECT * FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders);

-- NOT IN (SELECT)
SELECT * FROM customers
WHERE customer_id NOT IN (SELECT customer_id FROM orders);

-- between 
select * from products
where price between 10 and 15; 

--between text values 
select * from products 
where product_name BETWEEN 'Pavlova' AND 'Tofu';

--between date values 
select * from orders 
where order_date between '2023-04-12' and '2023-05-05';

-- aliases 
select customer_id as id
from customers;
-- as is optional, same result can be achieved without as 
select customer_id id 
from customers;

-- concatenate columns 
/*The AS keyword is often used when two or more fields are concatenated into one.
To concatenate two fields use ||.
*/
select product_name || unit as product 
from products;

-- using aliases with a space character 
select product_name as "My Great Products" 
from products; 






