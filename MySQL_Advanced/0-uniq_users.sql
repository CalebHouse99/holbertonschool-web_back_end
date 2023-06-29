--If the table exists, script doesn't fail
--can be executed on any database
CREATE TABLE IF NOT EXISTS users (
    id int,
    email text unique,
    name text 
);
