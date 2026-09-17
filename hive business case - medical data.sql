-- creating input table for medical visists table 

create table input_medical_visit (visit_id INT, patient_id INT, region STRING, visit_date DATE, diagnosis STRING, treatment STRING); 

-- loading value to the input medical visit 
insert into input_medical_visit VALUES 
(1,101,'North','2023-09-01','Hypertension','Medication'),
(2,102,'South','2023-09-02','Diabetes','Insulin'),
(3,103,'East','2023-09-03','Flu','Antiviral'),
(4,104,'North','2023-09-04','Asthma','Inhaler'),
(5,105,'South','2023-09-05','Hypertension','Medication');



-- Creating partition table for medical visit 
create table input_medical_visit (visit_id INT, patient_id INT, diagnosis STRING, treatment STRING) 
partitioned by  (visit_date DATE, region STRING) ;


-- creating non bucketed table  
create table input_medical_visit (visit_id INT, patient_id INT, region STRING, visit_date DATE, diagnosis STRING, 
treatment STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE; 


-- load data to non - bucketed input_medical visit 
load data local inpath 'medical_visit.csv' into table input_medical_visit; 

-- creating bucketed and partitioning table 
create table medical_visit (visit_id INT,  patient_id INT, diagnosis STRING, treatment STRING) 
partitioned by  (visit_date DATE, region STRING) clustered by (diagnosis, patient_id ) into 10 buckets 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' ;
