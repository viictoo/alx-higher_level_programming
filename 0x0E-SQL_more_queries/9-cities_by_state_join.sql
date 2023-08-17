-- a script that lists all cities contained in the database hbtn_0d_usa.
-- Each record displayS: cities.id - cities.name - states.name
-- Results ARE sorted in ascending order by cities.id
-- uses only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT
    cities.id,
    cities.name,
    states.name
FROM
    cities,
    states
WHERE
    cities.state_id = states.id
ORDER BY
    cities.id ASC;

-- SELECT
--     cities.id,
--     cities.name,
--     states.name
-- FROM
--     cities
--     RIGHT JOIN states ON cities.state_id = states.id
-- ORDER BY
--     id ASC;
