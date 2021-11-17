-- creates a database and user
-- user has select privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_02'@'localhost' IDENTIFIED BY 'user_od_2_pwd';
GRANT SELECT ON hbtn_0d_2 .* TO 'user_od_2'@'localhost';
FLUSH PRIVILEGES;
