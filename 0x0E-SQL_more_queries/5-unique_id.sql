-- a script that creates the table unique_id on an MySQL server.

-- unique_id description:
--     id INT with the default value 1 and must be unique
--     name VARCHAR(256)
-- The database name will be passed as an argument of the mysql command
-- If the table unique_id already exists, the script should not fail
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
