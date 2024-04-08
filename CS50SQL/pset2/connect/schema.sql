CREATE TABLE
    users (
        id INTEGER,
        username text NOT NULL UNIQUE,
        password text NOT NULL CHECK (length (password >= 8))
    );


