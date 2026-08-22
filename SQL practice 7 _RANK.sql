-- RANK Function Practice 
create table fruits (name varchar(255));

insert into fruits values ('apple'), ('apple'), ('orange'), ('grapes'), ('grapes'), ('watermelon');

select * from fruits;

--ROW_Number Function 
-- This is the simplest of all to understand. This function will just rank all selected rows in ascending order, 
--regardless of the values that were selects. 
SELECT name, ROW_NUMBER() OVER(ORDER BY name) from fruits;
