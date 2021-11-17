-- creating database and table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT AUTO_INCREMENT UNIQUE NOT NULL,
	state_id INT NOT NULL UNIQUE,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES hbtn_0d.states(id));

