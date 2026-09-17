- creating non partition table 

CREATE TABLE non_par_sales_data(sale_id INT, product_id INT, product_category STRING, customer_id INT, 
sale_amount FLOAT, sale_date Date, country STRING, region STRING); 


insert into non_par_sales_data VALUES 
(1,101,'Electronics',2001,500.00,'2023-08-01','US','North America'),
(2,102,'Electronics',2002,300.00,'2023-08-01','US','North America'),
(3,103,'Furniture',2003,700.00,'2023-08-02','UK','Europe'),
(4,104,'Furniture',2004,800.00,'2023-08-03','UK','Europe'),
(5, 105,'Clothing',2005,200.00,'2023-08-03','IN','Asia'),
(6,106,'Clothing',2006,600.00,'2023-08-03','IN','Asia');

-- creating partition table partitioned on sale_date, and country
CREATE TABLE partition_sales_data(sale_id INT, product_id INT, product_category STRING, customer_id INT, 
sale_amount FLOAT, region STRING) partitioned by (sale_date Date, country STRING); 

-- copying data from non partition table to partition table
insert overwrite table partition_sales_data partition (sale_date, country) select sale_id, product_id, product_category, customer_id, 
sale_amount, region, sale_date, country from non_par_sales_data; 

-- creating non-bucketed table 
CREATE TABLE non_buck_sales_data(sale_id INT, product_id INT, product_category STRING, customer_id INT, sale_amount FLOAT,
sale_date Date, country STRING, region STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE ; 

-- loading data from local to non bucketed table 
load data local inpath 'sales_data' into table non_buck_sales_data; 

-- creating bucketed table 
CREATE TABLE buck_sales_data(sale_id INT, product_id INT, product_category STRING, customer_id INT, sale_amount FLOAT ,
region STRING) 
partitioned by (sale_date Date, country STRING) clustered by (product_category, customer_id) into 10 BUCKETS
 ROW FORMAT DELIMITED FIELDS TERMINATED BY ','; 
 
 -- Inserting values to the bucketed table from the non-bucketed table 
 INSERT INTO buck_sales_data PARTITION (sale_date, country) select sale_id, product_id, product_category, customer_id, sale_amount,
 region, sale_date, country from non_buck_sales_data;
