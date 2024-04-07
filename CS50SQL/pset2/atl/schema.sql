CREATE TABLE
    passengers (
        "id" INTEGER,
        "first_name" TEXT,
        "last_name" TEXT,
        "age" INTEGER,
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

create table flights (
    "id" integer,
    "airline_id" integer,
    "from_airport" text,
    "to_airport" text,
    "departure_time" numeric,
    "arrival_time" numeric

)
