-- a script that lists all shows contained in the database hbtn_0d_tvshows.
-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- Link:
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql

    -- Each record display: tv_shows.title - tv_show_genres.genre_id
    -- Results sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
    -- If a show doesn’t have a genre, display NULL
    -- use only one SELECT statement
    -- The database name will be passed as an argument of the mysql command

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
