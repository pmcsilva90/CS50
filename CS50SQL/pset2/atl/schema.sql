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
        "name" TEXT UNIQUE NOT NULL
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
        "departure_hour" NUMERIC,
        "departure_minute" NUMERIC,
        "arrival_hour" NUMERIC,
        "arrival_minute" NUMERIC,
        PRIMARY KEY "id",
        FOREIGN KEY "airline_id" REFERENCES "airline" ("id")
    );
