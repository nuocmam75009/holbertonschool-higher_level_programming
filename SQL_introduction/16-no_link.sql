-- Lists all records of second_table
-- Don't list rows without 'name' value
-- Display score then name
-- Records listed by desc
SELECT records, name FROM second_table WHERE name IS NOT NULL ORDER BY records DESC;