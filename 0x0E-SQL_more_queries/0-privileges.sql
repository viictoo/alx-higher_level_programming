-- a script that lists all privileges of the MySQL users
-- Check if the user exists before revoking privileges
USE sys;
DELIMITER //
CREATE PROCEDURE ModifyUserPrivileges()
BEGIN
    DECLARE user_exists INT DEFAULT 0;

    -- Check if the user exists
    SELECT COUNT(*) INTO user_exists FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost';

    -- Revoke unwanted privileges if the user exists
    IF user_exists > 0 THEN
        REVOKE AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, BACKUP_ADMIN, BINLOG_ADMIN,
               FIREWALL_EXEMPT, GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN,
               SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN, XA_RECOVER_ADMIN
        FROM 'user_0d_1'@'localhost';
    END IF;

    SHOW GRANTS FOR 'user_0d_1'@'localhost';
    SHOW GRANTS FOR 'user_0d_2'@'localhost';
    -- -- Grant desired privileges
    -- GRANT BACKUP_ADMIN, BINLOG_ADMIN
    -- TO 'user_0d_1'@'localhost';

    -- Create the user and grant privileges if it doesn't exist
    -- IF user_exists = 0 THEN
    --     CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
    --     SET PASSWORD FOR 'user_0d_1'@'localhost' = 'user_0d_1_pwd';

        -- GRANT BACKUP_ADMIN, BINLOG_ADMIN
END;
//

DELIMITER ;

-- Call the stored procedure
CALL ModifyUserPrivileges();

-- SHOW GRANTS FOR 'user_0d_1'@'localhost';
-- SHOW GRANTS FOR 'user_0d_2'@'localhost';
