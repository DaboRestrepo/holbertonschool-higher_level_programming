-- List all the records of the table.
-- The records has to have name.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
