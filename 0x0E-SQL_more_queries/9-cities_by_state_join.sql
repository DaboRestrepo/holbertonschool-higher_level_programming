-- Display all the cities in the database.
SELECT id, cities.name, states.name
FROM cities NATURAL JOIN states
ORDER BY cities.id;
