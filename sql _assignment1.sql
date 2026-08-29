-- sql assessment 1 - Ghimire
-- Adding 1 to all tables to differentiate from the table that are already exists in the database .
CREATE TABLE customers1(
customer_id int, 
customer_name varchar(50),
city varchar(50)
); 

--Creating products table 
CREATE TABLE products1(
product_id int, 
product_name varchar(50),
category varchar(50),
price decimal(50)
);

-- creating orders table 
CREATE TABLE orders1(
order_id int, 
customer_id int, 
product_id int, 
quantity int, 
order_date date
); 
