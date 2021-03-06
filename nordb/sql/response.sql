/*
+-----------------------+
|RESPONSE TABLE CREATION|
+-----------------------+

This sql file has all the commands for creating a response table.

*/

--Create enum for response format 
CREATE TYPE response_format AS ENUM ('paz', 'fap');

--Create table command for response
CREATE TABLE response(
    id SERIAL PRIMARY KEY,
    creation_id INTEGER REFERENCES creation_info(id),
    file_name VARCHAR(64) UNIQUE,
    source VARCHAR(32),
    stage INTEGER,
    description VARCHAR(32),
    format RESPONSE_FORMAT NOT NULL,
    author VARCHAR(32)
);

--Enable row level security
ALTER TABLE response ENABLE ROW LEVEL SECURITY;
