-- a script that updates the score of Bob to 10 in the table second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
