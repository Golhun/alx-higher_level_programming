-- This script lists all records of the second_table without rows with no name value

-- Select records with a name value, displaying score and name, ordered by descending score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
