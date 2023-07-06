--can be executed on any database
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL PRIMARY KEY,
    email VARCHAR(256) NOT NULL UNIQUE,
    name VARCHAR(256)
);
