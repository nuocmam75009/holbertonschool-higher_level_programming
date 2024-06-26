-- Use database hbtn_0d_usa
-- list cities of california means ones that have name = 'cali'
-- but the id can be different.
-- results in ASC order by cities.id
SELECT id, name
FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = 'California');