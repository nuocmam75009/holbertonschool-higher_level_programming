-- Use database hbtn_0d_usa
-- list cities of california means ones that have name = 'cali'
-- but the id can be different.
-- results in ASC order by cities.id
SELECT name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;