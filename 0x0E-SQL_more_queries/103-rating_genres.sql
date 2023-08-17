-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
--     Each record displays: tv_genres.name - rating sum
--     Results are sorted in descending order by their rating
--     uses only one SELECT statement
--     The database name will be passed as an argument of the mysql command
SELECT
    tv_genres.name,
    SUM(rate) AS rating
FROM
    tv_show_ratings,
    tv_shows,
    tv_genres,
    tv_show_genres
WHERE
    tv_shows.id = tv_show_ratings.show_id
    AND tv_shows.id = tv_show_genres.show_id
    AND tv_genres.id = tv_show_genres.genre_id
GROUP BY
    tv_genres.id
ORDER BY
    rating DESC,
    tv_genres.name ASC;
