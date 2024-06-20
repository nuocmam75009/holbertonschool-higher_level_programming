-- Script that lists privileges of a user
-- SELECT user, host FROM mysql.user WHERE user IN ('user_0d_1', 'user_0d_2') AND host = 'localhost';
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0D_2'@'localhost';