-- Stored procedures 
/*--A stored procedure is a precompiled SQL code that can be saved and reused.
If you have an SQL query that you write over and over again, save it as a stored procedure, and then just call it to execute it.
A stored procedure can also have parameters, so it can act based on the parameter value(s) that is passed.*/
-- Key Benefits 
/*
Code Reusability - The same procedure can be called from various applications
Improved Performance - Stored procedures are precompiled and runs faster
Database Security - You can set users permission to run a specific procedure (limits direct access to tables)
Easy Maintenance - When updating a procedure, it automatically updates all its use
*/
-- Syntax
CREATE PROCEDURE procedure_name
  @param1 datatype,
  @param2 datatype
AS
BEGIN
  -- SQL_statements to be executed
  SELECT column1, column2
  FROM table_name
  WHERE columnN = @paramN;
END;

-- Drop stored procedure
Drop procedure procedure name;

DROP PROCEDURE IF EXISTS procedure_name; 

-- Example 
CREATE PROCEDURE GetCustomersByCity
  @City nvarchar(50)
AS
BEGIN
  SELECT * FROM Customers
  WHERE City = @City;
END;


