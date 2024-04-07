CREATE TABLE
    passengers (
        "id" INTEGER,
        "first_name" TEXT NOT NULL,
        "last_name" TEXT NOT NULL,
        "age" INTEGER NOT NULL,
        PRIMARY KEY ("id")
    );

CREATE TABLE
    check_ins (
        "id" INTEGER,
        "timestamp" NUMERIC NOT NULL DEFAULT CURRENT_TIMESTAMP,
        "passenger_id" INTEGER,
        "flight_id" INTEGER,
        PRIMARY KEY ("id"),
        FOREIGN KEY ("passenger_id") REFERENCES "passengers" ("id"),
        FOREIGN KEY ("flight_id") REFERENCES "flights" ("flight_id")
    );

CREATE TABLE
    airlines (
        "id" INTEGER,
        "name" TEXT UNIQUE NOT NULL,
        "concourse" TEXT NOT NULL CHECK (
            "concourse" IN ('A', 'B', 'C', 'D', 'E', 'F', 'T')
        ),
        PRIMARY KEY "id"
    );

CREATE TABLE
    flights (
        "id" INTEGER,
        "airline_id" INTEGER,
        "from_airport" TEXT NOT NULL,
        "to_airport" TEXT NOT NULL,
        "departure_date" DATE,
        "departure_hour" INTEGER CHECK ("departure_hour" >= 0 AND "departure_hour" < 24),
        "departure_minute" INTEGER CHECK ("departure_minute" >= 0 AND "departure_minute" < 60),
        "arrival_date" DATE,
        "arrival_hour" INTEGER CHECK ("arrival_hour" >= 0 AND "arrival_hour" < 24),
        "arrival_minute" INTEGER CHECK ("arrival_minute" >= 0 AND "arrival_minute" < 60),
        PRIMARY KEY "id",
        FOREIGN KEY "airline_id" REFERENCES "airline" ("id")
    );
