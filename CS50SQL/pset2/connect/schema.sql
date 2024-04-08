CREATE TABLE
    users (
        id INTEGER,
        username text NOT NULL UNIQUE,
        password text NOT NULL check (length(password >= 8))
    )
