
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


-- creating partitioned and bucketed table 

CREATE TABLE data_usage (
usage_id INT,
customer_id INT, 
data_used FLOAT COMMENT "In GB" 
 ) 
PARTITIONED BY (usage_date DATE, region STRING) clustered by (customer_id) into 4 buckets
ROW FORMAT DELIMITED FIELDS TERMINATED BY ","; 

-- inserting data from non bucketed nbct_data_usage table to bucketed and partitioned data_usage table 
INSERT OVERWRITE TABLE data_usage 
partition (usage_date = '2023-08-01', region = 'North') 
SELECT usage_id, customer_id, data_used
FROM nbct_data_usage WHERE usage_date = '2023-08-01' and region = 'North'; 


--non stricting partition mode 
set hive.exec.dynamic.partition.mode=nonstrict; 

-- inserting remaining data from the non bucketed table to bucketed table 
INSERT OVERWRITE TABLE data_usage
PARTITION (usage_date, region) 
SELECT usage_id, customer_id, data_used,usage_date, region 
FROM nbct_data_usage; 

-- SMS Data Table 
-- creating non bucketed table for sms data table 
create table nbct_sms_data (
sms_id INT, 
customer_id INT, 
sms_count INT, 
region STRING, 
sms_date DATE) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY "," stored as TEXTFILE; 

-- Creating local data file 
nano sms_data.csv 

-- sample data in the file 
1,101,5,North,2023-08-01
2,102,10,South,2023-08-02
3,103,8,East,2023-08-03
4,104,7,West,2023-08-04
5,105,15,North,2023-08-05

-- loading data into the non-bucketed table from the local file 
load data local inpath 'sms_data.csv' into table nbct_sms_data; 

-- creating bucketed and partitioned table 

create table sms_data (
sms_id INT, 
customer_id INT, 
sms_count INT) 
partitioned BY (sms_date DATE, region STRING) 
clustered by (customer_id) into 4 buckets
ROW FORMAT DELIMITED FIELDS TERMINATED BY "," stored as TEXTFILE; 


-- turning off strict dynamic partition mode 
set hive.exec.dynamic.partition.mode = nonstrict;

-- loading data from non bucketed table to bucketed and partitioned table 

insert OVERWRITE table sms_data 
PARTITION (sms_date, region) SELECT sms_id, customer_id, sms_count, sms_date, region 
FROM nbct_sms_data;

-- Query Optimization using partition and bucketing 
--a. Call Durations by Region and Date
	--	To query total call durations for a specific region and date:
SELECT  call_date, region, SUM(call_duration) AS total_duration 
FROM call_data 
WHERE call_date = '2023-08-01' AND region = 'North'
GROUP BY call_date, region; 

--b. Top data users by Region
	-- To find the dop data users in a specific region:
	
SELECT customer_id, SUM(data_used) AS total_data
FROM data_usage
WHERE region = 'North'
GROUP BY customer_id
ORDER BY total_data DESC;

--c. SMS usage trends by region 
	-- to analyze SMS usage trends in specific region:
SELECT customer_id, SUM(sms_count) AS total_sms 
FROM sms_data
WHERE region = 'North'
group by customer_id; 

-- Advantage of Partitioning and Bucketing 
	--* Partitioning: - Optimizes data retrieval for time-based and regional queries, reducing scan time for large datasets
	--* Budketing: - Improves query performance for specific customer-centric queries, helping analyze data for individual customers in telecom operations
	
	-- Conclusion 
	/* Partitioning and bucketing in Hive for telecommunication data improves query performance by optimizing data storage and retrieval. 
		Partitioning by call_date, usage_date, and sms_date with region helps in faster regional and time-based queries, 
		while bucketing by customer_id speeds up customer-centric queries, making it easier to identify trends and heavy data users.
		*/ 
