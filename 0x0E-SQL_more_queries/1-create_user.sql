-- Create MySQL server user
-- user have all previleges on the server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT USAGE ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
