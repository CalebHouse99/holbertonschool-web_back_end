--If the table exists, script doesn't fail
--can be executed on any database
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL,
    email VARCHAR(256) NOT NULL UNIQUE,
    name VARCHAR(256)
);
