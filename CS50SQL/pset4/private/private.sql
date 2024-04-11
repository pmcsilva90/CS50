CREATE TABLE
    triplets (
        sentence_num INTEGER NOT NULL,
        char_num INTEGER NOT NULL,
        message_len INTEGER NOT NULL
    );

INSERT INTO
    triplets (sentence_num, char_num, message_len)
VALUES
    (14, 98, 4),
    (114, 3, 5),
    (618, 72, 9),
    (630, 7, 3),
    (932, 12, 5),
    (2230, 50, 7),
    (2346, 44, 10),
    (3041, 14, 5);

CREATE VIEW
    triplet1 AS
SELECT
    *
FROM
    sentences
WHERE
    id IN (14, 114, 618, 630, 932, 2230, 2346, 3041);

SELECT
    substr (sentence,)
