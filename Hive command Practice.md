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

