
-- creating non-partition call data table 
create table npt_call_data (
call_id INT, 
customer_id INT, 
call_duration FLOAT, 
region STRING, 
call_date DATE); 

-- Creating partition call data table 

create table pt_call_data (
 call_id INT, 
customer_id INT, 
call_duration FLOAT 
) partitioned by (call_date DATE,region STRING);

-- creating non-bucketed table 
create table nbct_call_data (
call_id INT, 
customer_id INT, 
call_duration FLOAT, 
region STRING, 
call_date DATE) ROW FORMAT DELIMITED FIELDS TERMINATED BY "," stored as TEXTFILE ;

-- Create the sample data file in local path 
nano call_data.csv 
-- sample data 
1,101,15.5,North,2023-08-01
2,102,20.2,South,2023-08-02
3,103,5.7,East,2023-08-03
4,104,12.4,West,2023-08-04
5,105,25.0,North,2023-08-05


-- loading the data from the local file to non-bucketed table in hive 
load data local inpath  'call_data.csv' into table nbct_call_data; 


-- creating partitioned and bucketed table 

create table call_data (
call_id INT, 
customer_id INT, 
call_duration FLOAT 
) partitioned by  (call_date DATE, region STRING) clustered by (customer_id) into 4 buckets 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ","; 

-- Loading data from the non-bucketed nbct_data_call table into bucketed call_data table. 

insert into call_data PARTITION (call_date, region) SELECT call_id, customer_id, call_duration, call_date, region from nbct_call_data; 


--Data usage table 
-- creating non bucketed data usage table 
CREATE TABLE nbct_data_usage (
usage_id INT,
customer_id INT, 
data_used FLOAT COMMENT "In GB", 
region STRING, 
usage_date DATE ) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY "," stored as TEXTFILE; 

-- Creating the local data file in local path 
nano data_usage.csv 

-- sample data for the data_usage.csv
1,101,2.5,North,2023-08-01
2,102,3.0,South,2023-08-02
3,103,1.2,East,2023-08-03
4,104,5.5,West,2023-08-04
5,105,10.0,North,2023-08-05

-- loading the table from the local file 
load data local inpath 'data_usage.csv' into table nbct_data_usage; 

