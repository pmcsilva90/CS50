CREATE TABLE
    ingredients (
        id INTEGER,
        name TEXT NOT NULL UNIQUE,
        unit TEXT NOT NULL,
        unit_qty INTEGER NOT NULL,
        price_per_unit NUMERIC NOT NULL PRIMARY KEY (id)
    );

CREATE TABLE
    donuts (
        id INTEGER,
        name TEXT NOT NULL,
        gluten_free TEXT NOT NULL CHECK (gluten_free IN ('Yes', 'No')),
        price_per_donut NUMERIC NOT NULL,
        PRIMARY KEY (id)
    );
CREATE TABLE
    orders (
        id INTEGER,
        timestamp NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
        instore_online TEXT NOT NULL CHECK (instore_online IN ('In store', 'Online')),
        customer_id INTEGER,
        cost NUMERIC NOT NULL CHECK(cost != 0),
        payment_method TEXT NOT NULL CHECK(cost IN('Cash', 'Card'))
        PRIMARY KEY (id),
        FOREGIN KEY (customer_id) REFERENCES customers (id)
    );
CREATE TABLE
    customers (
        id INTEGER,
        first_name TEXT,
        last_name TEXT,
        PRIMARY KEY (id)
    );
