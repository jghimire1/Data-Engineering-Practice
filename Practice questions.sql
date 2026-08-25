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

--Write an SQL query to report the name and bonus amount of each employee with a bonus less than 1000.
--Return the result table in any order
 select employee.name, bonus.bonus from employee
 left join bonus on bonus.empID = employee.empID 
 where bonus < 1000 
 or bonus is null; 

 --creating table customer 
 create table customer(
id int, 
name varchar, 
referee_id int
);

--inserting values to customer table 
insert into customer (id, name, referee_id)
VALUES 
(1, 'Will', null),
(2, 'Jane', null),
(3, 'Alex', 2),
(4, 'Bill', null),
(5, 'Zack', 1),
(1, 'Mark', 2); 

--Write an SQL query to report the names of the customer that are not referred by the customer with id = 2.
Select name from customer where referee_id != 2 or referee_id is null;

--creating student table 
create table student (
student varchar,
class varchar
); 
