-- Lists the number of records with same scores
-- in second_table
SELECT score COUNT(*) AS number GROUP BY score FROM second_table ORDER BY number DESC;