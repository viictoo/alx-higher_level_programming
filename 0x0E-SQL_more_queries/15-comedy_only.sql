-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.

--     The tv_genres table contains only one record where name = Comedy (but the id can be different)
--     Each record displays: tv_shows.title
--     Results sorted in ascending order by the show title
--     Uses only one SELECT statement
--     The database name will be passed as an argument of the mysql command

SELECT tv_shows.title
FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_genres.id = tv_show_genres.genre_id
AND tv_show_genres.show_id = tv_shows.id
AND tv_genres.name = "Comedy"
ORDER BY tv_shows.title  ASC;
