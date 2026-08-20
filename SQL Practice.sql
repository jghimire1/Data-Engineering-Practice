-- create table 
CREATE TABLE cars (
  brand VARCHAR(255),
  model VARCHAR(255),
  year INT
);

INSERT INTO cars (brand, model, year)
VALUES ('Ford', 'Mustang', 1964);

SELECT * FROM cars;

--Specify columns

SELECT brand, year FROM cars; 

--Alter table statement 
ALTER TABLE cars ADD color VARCHAR(255);

Update cars 
SET color = 'red'
WHERE brand = 'Ford';
-- Drop column
ALTER TABLE cars
DROP COLUMN color;

-- Delete the records of Ford 
DELETE FROM cars
WHERE brand = 'Ford';

-- Delete the cars table 
Drop table cars;
