-- This script lists all records with a score >= 10 in the second_table

-- Select records with a score >= 10 from the second_table, ordering by score (top first)
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
