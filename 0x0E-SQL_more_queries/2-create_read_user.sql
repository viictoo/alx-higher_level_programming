-- a script that creates the MySQL server user user_0d_1.

-- user_0d_1 given all privileges on your MySQL server
-- user_0d_1 password set to user_0d_1_pwd
-- if the user user_0d_1 already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
