--     id, which represents the unique ID of the meteorite.
--     name, which represents the given name of the meteorite.
--     class, which is the classification of the meteorite, according to the traditional classification scheme.
--     mass, which is the weight of the meteorite, in grams.
--     discovery, which is either “Fell” or “Found”. “Fell” indicates the meteorite was seen falling to Earth, whereas “Found” indicates the meteorite was found only after landing on Earth.
--     year, which is the year in which the the meteorite was discovered.
--     lat, which is the latitude at which the meteorite landed.
--     long, which is the longitude at which the meteorite landed.
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
    -- Keep in mind that not all columns in the CSV should end up in the final table!
    -- To consider the data in the meteorites table clean, you should ensure…
    --     Any empty values in meteorites.csv are represented by NULL in the meteorites table.
    --         Keep in mind that the mass, year, lat, and long columns have empty values in the CSV.
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

--     All columns with decimal values (e.g., 70.4777) should be rounded to the nearest hundredths place (e.g., 70.4777 becomes 70.48).
--         Keep in mind that the mass, lat, and long columns have decimal values.
update

--     All meteorites with the nametype “Relict” are not included in the meteorites table.
--     The meteorites are sorted by year, oldest to newest, and then—if any two meteorites landed in the same year—by name, in alphabetical order.
--     You’ve updated the IDs of the meteorites from meteorites.csv, according to the order specified in #4.
--         The id of the meteorites should start at 1, beginning with the meteorite that landed in the oldest year and is the first in alphabetical order for that year.
