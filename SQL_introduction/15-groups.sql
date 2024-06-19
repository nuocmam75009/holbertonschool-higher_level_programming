-- Lists the number of records with same scores
-- in second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;