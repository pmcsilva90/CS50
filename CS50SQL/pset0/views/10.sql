SELECT "print_number" AS "Print Number", "english_title" AS "English Titles Referencing Provinces", "artist" AS "Artist" FROM "views" WHERE "english_title" LIKE '%province%' ORDER BY "print_number";
