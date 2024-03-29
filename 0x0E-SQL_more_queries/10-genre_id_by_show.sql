-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download
-- Link:
-- https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
-- Write a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows,
    tv_show_genres
WHERE
    tv_shows.id = tv_show_genres.show_id
ORDER BY
    tv_shows.title,
    tv_show_genres.genre_id;

-- SELECT
--     tv_shows.title,
--     tv_show_genres.genre_id
-- FROM
--     tv_shows
--     RIGHT JOIN tv_show_genres ON tv_shows.id = tv_sho w_genres.show_id
-- ORDER BY
--     tv_shows.title,
--     tv_show_genres.genre_id;
