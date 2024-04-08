CREATE TABLE
    users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        password TEXT NOT NULL CHECK (length (password >= 8))
    );

CREATE TABLE
    education_institutions (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT,
        country TEXT NOT NULL,
        year_founded INTEGER
    );

CREATE TABLE
    companies (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        industry TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT,
        country TEXT NOT NULL
    );

CREATE TABLE
    users_connections (
        user1_id INTEGER,
        user2_id INTEGER,
        FOREIGN KEY (user1_id) REFERENCES users (id),
        FOREIGN KEY (user2_id) REFERENCES users (id)
    );

CREATE TABLE
    users_education (
        user_id INTEGER,
        institution_id INTEGER,
        start_date DATE,
        end_date DATE,
        degree TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (institution_id) REFERENCES education_institutions (id)
    );

CREATE TABLE
    users_employment (
        user_id INTEGER,
        company_id INTEGER,
        start_date DATE,
        end_date DATE,
        role TEXT,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (company_id) REFERENCES companies (id)
    );
