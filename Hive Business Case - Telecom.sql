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
