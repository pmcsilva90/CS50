CREATE TABLE
    ingredients (
        id INTEGER,
        name TEXT NOT NULL UNIQUE,
        unit TEXT NOT NULL,
        unit_qty INTEGER NOT NULL,
        price_per_unit NUMERIC NOT NULL
        PRIMARY KEY (id)
    );

CREATE TABLE donuts (
    id INTEGER,
    name TEXT NOT NULL,
    gluten_free TEXT NOT NULL CHECK(gluten_free IN ('yes', 'no')),
    price_per_donut NUMERIC NOT NULL,
    PRIMARY KEY (id)
)
