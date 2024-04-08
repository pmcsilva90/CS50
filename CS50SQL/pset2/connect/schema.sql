CREATE TABLE
    users (
        id INTEGER PRIMARY key,
        username text NOT NULL UNIQUE,
        first_name text NOT NULL,
        last_name text NOT NULL,
        password text NOT NULL CHECK (length (password >= 8)),
    );

CREATE TABLE
    education_institutions (
        id INTEGER PRIMARY key,
        type text NOT NULL,
        location text,
        founded INTEGER
    );

CREATE TABLE
    companies (
        id INTEGER PRIMARY key,
        name text UNIQUE NOT NULL,
        industry text NOT NULL,
        location text NOT NULL
    );

CREATE TABLE
    users_connections (
        user1_id INTEGER,
        user2_id INTEGER,
        FOREIGN key (user1_id) REFERENCES users (id),
        FOREIGN key (user2_id) REFERENCES users (id)
    );

CREATE TABLE
    users_education (
        user_id INTEGER,
        institution_id INTEGER,
        start_date DATE,
        end_date DATE,
        degree text,
        FOREIGN key user_id REFERENCES users (id),
        FOREIGN key institution_id REFERENCES education_institutions (id)
    );

CREATE TABLE
    users_employment (
        user_id INTEGER,
        company_id INTEGER,
        stard_date DATE,
        end_date DATE,
        role text,
        FOREIGN key user_id REFERENCES users (id),
        FOREIGN key company_id REFERENCES companies (id)
    );
