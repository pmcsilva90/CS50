CREATE TABLE
    users (
        id INTEGER PRIMARY key,
        username text NOT NULL UNIQUE,
        first_name text NOT NULL,
        last_name text NOT NULL,
        password text NOT NULL CHECK (length (password >= 8)),
    );

create table 

CREATE TABLE
    education (
        id INTEGER PRIMARY key,
        type text NOT NULL,
        location text,
        founded INTEGER
    )
CREATE TABLE
    companies (
        id INTEGER PRIMARY key,
        name text UNIQUE NOT NULL,
        industry text NOT NULL,
        location text NOT NULL
    )
