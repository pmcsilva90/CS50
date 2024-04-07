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
        PRIMARY key ("id"),
        FOREIGN key ("passenger_id") REFERENCES "passengers" ("id"),
        FOREIGN key ("flight_id") REFERENCES "flights" ("flight_id")
    );

CREATE TABLE
    airlines (
        "id" INTEGER,
        "concourse" text NOT NULL CHECK (
            "concourse" IN ('A', 'B', 'C', 'D', 'E', 'F', 'T')
        ),
        PRIMARY key "id"
    );

CREATE TABLE
    flights (
        "id" INTEGER,
        "airline_id" INTEGER,
        "from_airport" text NOT NULL,
        "to_airport" text NOT NULL,
        "departure_time" NUMERIC NOT NULL datetime,
        "arrival_time" NUMERIC NOT NULL datetime,
    );
