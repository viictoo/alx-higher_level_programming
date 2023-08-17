-- a script that lists all privileges of the MySQL users
-- Revoke unwanted privileges
REVOKE AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, BACKUP_ADMIN, BINLOG_ADMIN,
       FIREWALL_EXEMPT, GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN,
       SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN, XA_RECOVER_ADMIN
FROM 'user_0d_1'@'localhost';

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
