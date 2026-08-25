--creating employee 
CREATE TABLE Employee (
empId int,
name varchar,
supervisor int, 
salary int) ;

-- creating bonus table 
create table bonus (
empID int, 
bonus int
);

-- insert values to the employee table 
INSERT INTO Employee (empId, name, supervisor, salary)
values 
(3, 'Brad', null , 4000),
 (1, 'John', 3, 1000),
 (2, 'Dan', 3, 2000),
 (4, 'Thomas', 3, 4000);

 -- insert into bous table 
 insert into bonus (empID, bonus)
 values 
 (2, 500),
 (4, 2000);
 
select * from employee;

select * from bonus;
