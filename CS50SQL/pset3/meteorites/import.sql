.import -csv meteorites.csv temp

CREATE TABLE
    "meteorites" (
        "id" INTEGER,
        "name" TEXT NOT NULL UNIQUE,
        "class" TEXT,
        "mass" REAL,
        "discovery" TEXT CHECK ("discovery" IN ('Found', 'Fell')),
        "year" INTEGER,
        "lat" REAL,
        "long" REAL,
        PRIMARY KEY ("id")
    );

-- empty values in meteorites.csv are represented by NULL in the meteorites table.
-- mass, year, lat, and long columns have empty values in the CSV.
UPDATE temp
SET
    mass = NULL
WHERE
    mass = '';

UPDATE temp
SET
    year = NULL
WHERE
    year = '';

UPDATE temp
SET
    lat = NULL
WHERE
    lat = '';

UPDATE temp
SET
    long = NULL
WHERE
    long = '';

-- All columns with decimal values (e.g., 70.4777) should be rounded to the nearest hundredths place (e.g., 70.4777 becomes 70.48).
-- mass, lat, and long columns have decimal values.
UPDATE temp
SET
    mass = ROUND(mass, 2);

UPDATE temp
SET
    lat = ROUND(lat, 2);

UPDATE temp
SET
    long = ROUND(long, 2);

-- All meteorites with the nametype “Relict” are not included in the meteorites table.
DELETE FROM temp
WHERE
    nametype = 'Relict';

-- The meteorites are sorted by year, oldest to newest, and then—if any two meteorites landed in the same year—by name, in alphabetical order.
INSERT INTO
    meteorites (name, class, mass, discovery, year, lat, long)
SELECT
    name,
    class,
    mass,
    discovery,
    year,
    lat,
    long
FROM
    temp
ORDER BY
    year,
    name;

DROP TABLE temp;
