SELECT "title", "season", "episode_in_season", "air_date" FROM "episodes" WHERE "air_date" LIKE '2007%' OR "air_date" LIKE '2017%' ORDER BY "air_date" DESC;
