
-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

-- Import the database dump from hbtn_0d_tvshows to your MySQL server:
-- Link:
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql

--     Each record should display: <TV Show genre> - <Number of shows linked to this genre>
--     First column must be called genre
--     Second column must be called number_of_shows
--     Don’t display a genre that doesn’t have any shows linked
--     Results must be sorted in descending order by the number of shows linked
--     You can use only one SELECT statement
--     The database name will be passed as an argument of the mysql command


SELECT name AS "genre", COUNT(name) AS "number_of_shows" FROM tv_genres, tv_show_genres WHERE tv_genres.id = tv_show_genres.genre_id GROUP BY name ORDER BY number_of_shows DESC;
