# Hive command history: 
    startApps$ cat ~/.hivehistory
    show databases;
    show tables;
    CREATE TABLE partition_date(column1 string) partitioned by (day string, event string);
    CREATE TABLE non_partitioned_date1(column1 string, day string,event string);
    insert overwrite table partition_date partition(day,event) select * from non_partitioned_date1;
    set hive.exec.dynamic.partition.mode=nonstrict;
    insert overwrite table partition_date partition(day,event) select * from non_partitioned_date1;
    show tables;
    show partitions partition_date;
    insert overwrite table partition_date partition(day,event) select * from non_partitioned_date1;
    quit;
    select * from non_partitioned_date1;
    insert into non_partitioned_date1 values('abc', '2000-01-01','e1'),('abc', '2000-01-02','e1');
    select * from test;
    insert into non_partitioned_date1 values('abc', '2000-01-01','e1'),('abc', '2000-01-02','e1');
    select * from non_partitioned_date1;
    insert overwrite table partition_date partition(day,event) select * from non_partitioned_date1;
    set hive.exec.dynamic.partition.mode=nonstrict;
    insert overwrite table partition_date partition(day,event) select * from non_partitioned_date1;
    show partitions partition_date;
    insert overwrite table partition_date partition(day,event) select * from non_partitioned_date1;
    insert into non_partitioned_date1 values('abc', '1999-12-20','e1'),('abc', '2000-01-01','e1');
    set hive.exec.dynamic.partition.mode=nonstrict;
    insert overwrite table partition_date partition(day,event) select * from non_partitioned_date1;
    show partitions partition_date;
    show tables;
    quit;
    show databases;
    use default;
    show tables;
    select * from partition_date;
    create database xyz;
    use xyz;
    create external table customer(id int, name string, dob date, time1 timestamp) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/data/test/text';
    show tables;
    select * from customer;
    drop table customer;
    show table; 
    show tables;
    create external table customer(id int, name string, dob date, time1 timestamp) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' LOCATION '/data/test/text';
    show tables;
    create table emp(empId int, empName string, doi date);
    insert into emp values(1,'vishal','2009-01-01');
    select * from emp;
    drop table emp;
    show tables;
    create table emp(empId int, empName string, doj date);
    insert into emp values(1,'vishal','2009-01-01');
    show tables;
    describe customer;
    create emp1(empId int, empName String, doj date);
    create table  emp1(empId int, empName String, doj date);
    show tables;
    insert overwrite table emp1 select * from emp; 
    select * from  emp1;
    insert into table emp1 select * from emp ;
    select * from  emp1;
    insert overwrite table emp1 select * from emp; 
    select * from  emp1;
    CREATE TABLE non_partitioned_date1(column1 string, day string,event string);
    insert into non_partitioned_date1 values('abc', '2000-01-01','e1') , ('abc', '2000-01-02','e1'), ('abc', '1999-12-20','e1') ,('abc', '2000-01-01','e1');
    select * from non_partitioned_date1;
    CREATE TABLE partition_date(column1 string) partitioned by (day string, event string);
    insert overwrite table partition_date partition(day,event) select column1,day,event from non_partitioned_date1;
    set hive.exec.dynamic.partition.mode=nonstrict;
    insert overwrite table partition_date partition(day,event) select column1,day,event from non_partitioned_date1;
    select * from partition_date;
    show partitions partition_date;
    CREATE TABLE partition_date_1(column1 string) partitioned by (day string, event string);
    insert overwrite table partition_date_1 partition(day,event) select column1,event,day from non_partitioned_date1;
    show partitions partition_date_1;
    alter table partition_date DROP PARTITION (day = '2000-01-01', event = 'e1');
    show partitions partition_date;

# create bucket in hive 
    create table input_table (Street string,
    City string,
    Zip string,
    State string,
    Beds string,
    Baths string,
    Sq_feet int,
    flat_type string,
    Price int) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
    STORED AS TEXTFILE;
    
    load data local inpath 'realstatewh.csv' into table input_table;
    
    SET hive.enforce.bucketing = true;
    set hive.exec.dynamic.partition.mode=nonstrict;
    
    
    create table bucket_table(Street string,
    Zip string,
    State string,
    Beds string,
    Baths string,
    Sq_feet int,
    flat_type string,
    Price int) partitioned by(city string) clustered by (street) into 4 buckets ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
    
    insert into table bucket_table partition(city) select street,zip,state,beds,baths,sq_feet,flat_type,price,city from input_table;
    
        

    

    
