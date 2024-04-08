CREATE TABLE
    users (
        id INTEGER,
        username text NOT NULL UNIQUE,
        password text NOT NULL CHECK (length (password >= 8)),
        PRIMARY key id
    );

CREATE TABLE
    education (
        id INTEGER,
        type text NOT NULL,
        location text
        founded integer
        primary key

    )
