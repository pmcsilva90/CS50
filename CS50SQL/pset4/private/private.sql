CREATE TABLE
    triplets (
        sentence_num INTEGER NOT NULL,
        char_num INTEGER NOT NULL,
        message_len INTEGER NOT NULL
    );


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
