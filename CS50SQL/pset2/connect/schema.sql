CREATE TABLE
    users (
        id INTEGER PRIMARY key,
        username text NOT NULL UNIQUE,
        first_name text NOT NULL,
        last_name text NOT NULL,
        password text NOT NULL CHECK (length (password >= 8)),
    );

create table people_connections(
    user_id1 integer foreign key references users(id),
    user_id2 integer foreign key references users(id),


)

CREATE TABLE
    institutions (
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
