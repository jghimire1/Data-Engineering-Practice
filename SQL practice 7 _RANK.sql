-- RANK Function Practice 
create table fruits (name varchar(255));

insert into fruits values ('apple'), ('apple'), ('orange'), ('grapes'), ('grapes'), ('watermelon');

select * from fruits;

--ROW_Number Function 
-- This is the simplest of all to understand. This function will just rank all selected rows in ascending order, 
--regardless of the values that were selects. 
SELECT name, ROW_NUMBER() OVER(ORDER BY name) from fruits;

-- RANK FUNCTION 
/* This function is very similar to the ROW_NUMBER() function. 
The only difference is that identical rows are marked with the same rank. 
Also, please note that if the function skipped a number while ranking (because of row similarity), 
that rank will be skipped.*/
SELECT name, RANK() OVER (ORDER BY name) from fruits;

--DENSE_RANK Function
--when using DENSE_RANK, the same rules apply as we described for RANK(), 
--with one difference - when similar rows are detecte, the next rank in line isn't skipped.
select name, DENSE_RANK() OVER (order by name) from fruits;

--creating new table to further evaluate the RANK Functions. 
create table ExamResult
(studentName varchar(70),
subject varchar(20),
Marks int
);

select * from examresult;

insert into examresult values ('Lily', 'Maths',65);
insert into examresult values ('Lily', 'Science', 80);
insert into examresult values ('Lily','English',70);
insert into examresult values ('Isabella', 'Maths', 50);

INSERT INTO ExamResult
VALUES
('Isabella',
'Science',
70
);
INSERT INTO ExamResult
VALUES
('Isabella',
'english',
90
);
INSERT INTO ExamResult
VALUES
('Olivia',
'Maths',
55
);
INSERT INTO ExamResult
VALUES
('Olivia',
'Science',
60
);
INSERT INTO ExamResult
VALUES
('Olivia',
'English',
89
);

--Query to get rowNum for the students as per their marks. 

select studentname, subject, marks,
row_number() over (order by marks) RowNumber
from examresult;

--rank order 
SELECT StudentName, Subject, marks, 
ROW_NUMBER()OVER (ORDER BY Marks) RowNumber
From ExamResult;

-- Check rank5 in output
-- use partition BY StudentName clause to perfomr calculations on each student group 
-- each subset should get rank as per their marks in descending order 
-- the result set uses order by clause to sort results on studentname and their rank 

SELECT Studentname, subject, marks, 
RANK() OVER(PARTITION BY studentname ORDER BY Marks DESC) RANK 
FROM examresult
ORDER BY studentname, Rank;

--DenseRank() SQL Rank function 
SELECT Studentname, marks, subject,
DENSE_RANK() OVER (ORDER BY Marks DESC) RANK 
FROM examresult 
order by RANK;

--CHECK rank 4 and 5 
--Partition by 
UPDATE examresult set marks = 70 where studentname = 'Isabella' and subject = 'Maths';

select studentname, subject, marks, 
DENSE_RANK() OVER(Partition by studentname order by marks) Rank
From ExamResult
ORDER BY studentName, Rank; 

--check rank 1 and 2
select studentName, Subject, Marks, 
RANK() OVER (PARTITION BY StudentName ORDER BY Marks) Rank 
FROM ExamResult
ORDER BY StudentName, Rank; 
--check rank and 3
-- CTE (Commom Table Expressions)
with t1 as (
SELECT Studentname, subject, marks, 
RANK()OVER (PARTITION BY studentName ORDER BY Marks) Rank
From ExamResult
ORDER BY StudentName, Rank
)
select * from t1 where Rank = 3 ;

-- Multiple CTE 
with t1 as (
SELECT StudentName, Subject, Marks, 
RANK() OVER(PARTITION BY StudentName ORDER BY Marks) Rank
From ExamResult
ORDER BY StudentName, Rank
), 
t2 as (select StudentName, Rank from t1)
SELECT * from t2 where Rank = 1;




