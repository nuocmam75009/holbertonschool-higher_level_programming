-- Lists the number of records with same scores
-- in second_table
SELECT score COUNT(*) AS number GROUP BY score FROM second_table WHERE score ORDER BY number DESC;