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

--q1: Show all customers from Mumbai
select * from customers1 
where city = 'Mumbai';

--Q2: Show all products with price greater than 1000
SELECT * FROM products1
WHERE price > 1000;

--Q3: Show all electronics products
SELECT * FROM products1
WHERE category = 'Electronics';

--Q4: Show all orders placed after 2026-01-14
SELECT * FROM orders1
WHERE ORDER_DATE > '2026-01-14';

--Q5: Display customer name and order date for all orders. 
SELECT c.customer_name, o.order_date 
from customers1 c join orders1 o ON c.customer_id = o.customer_id; 
--Q6: Show customer name, product name, quantity ordered 
SELECT c.customer_name, p.product_name, o.quantity
FROM customers1 c JOIN orders1 o ON c.customer_id = o.customer_id 
JOIN products1 p ON p.product_ID = o.product_ID;

--Q7: Display all customers who purchased laptop 
SELECT c.customer_name, p.product_name
FROM customers1 c JOIN orders1 o ON c.customer_id = o.customer_id 
JOIN products1 p ON p.product_ID = o.product_ID
where product_name = 'Laptop';
--Q8: Show total amount spent for each order 
Select o.order_id, p.price * o.quantity as total_amount from orders1 o
JOIN products1 p ON O.product_id = p.product_id
GROUP BY order_id, total_amount 
Order BY order_id; 

-- Q9: Find total quantity ordered for each product 
SELECT product_id, SUM(quantity) as total_quantity_ordered from orders1
GROUP BY product_id
ORDER BY product_id; 

--Q10: find toal sales amount for each category. 
select p.category, Sum(p.price * o.quantity) as total_sales from orders1 o 
join products1 p ON o.product_id = p.product_id
GROUP BY category; 

--Q11: Find total number of orders placed by each customer.

Select c.customer_name,  COUNT(o.order_id) as total_orders
From orders1 o 
JOIN customers1 c ON c.customer_id = o.customer_id
GROUP BY Customer_name; 

--Q12: Show average product price by category 
SELECT category, 
ROUND(AVG(price), 2) AS Avg_price
FROM products1
Group by Category; 

--Q13: Show categories where total sales amount is greater than 50000.

select p.category, Sum(p.price * o.quantity) as total_sales 
from orders1 o 
join products1 p ON o.product_id = p.product_id
GROUP BY p.category
HAVING SUM(p.price * o.quantity)> 50000; 

--Q14: Find customers who placed more than 2 orders
Select c.customer_name,  COUNT(o.order_id) as total_orders
From orders1 o 
JOIN customers1 c ON c.customer_id = o.customer_id
GROUP BY C.Customer_name
HAVING COUNT(o.order_id) > 2; 

