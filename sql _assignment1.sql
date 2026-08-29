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

-- Inserting sample data to the previously created tables 
INSERT INTO customers1 VALUES 
(1, 'Rahus', 'Mumbai'),
(2,'Anjali', 'Delhi'),
(3, 'Aman', 'Pune'),
(4, 'Sneha', 'Banglore'),
(5, 'Karan', 'Mumbai');

INSERT INTO products1 VALUES
(101, 'Laptop', 'Electronics', 70000),
(102, 'Phone', 'Electronics', 40000),
(103, 'Chair', 'Furniture', 5000),
(104, 'Desk', 'Furniture', 12000),
(105, 'Headphones', 'Electronics', 3000);

INSERT INTO orders1 VALUES
(1001, 1, 101, 1, '2026-01-10'),
(1002, 1, 105, 2, '2026-01-11'),
(1003, 2, 102, 1, '2026-01-12'),
(1004, 3, 103, 4, '2026-01-13'),
(1005, 4, 104, 1, '2026-01-14'),
(1006, 5, 101, 1, '2026-01-15'),
(1007, 2, 105, 3, '2026-01-16'),
(1008, 3, 102, 1, '2026-01-17'),
(1009, 1, 103, 2, '2026-01-18'),
(1010, 4, 105, 5, '2026-01-19');
