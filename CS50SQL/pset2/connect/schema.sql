CREATE TABLE
    users (
        id INTEGER,
        username text NOT NULL UNIQUE,
        first_name text not null,
        last_name text not null,

        password text NOT NULL CHECK (length (password >= 8)),
        PRIMARY key id
    );

CREATE TABLE
    education (
        id INTEGER primary key,
        type text NOT NULL,
        location text,
        founded integer

    )

    create table companies (
        id integer primary key,
        name text unique not null,
        industry text not null,
        location text not null
    )
