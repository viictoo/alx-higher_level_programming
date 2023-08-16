-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Link:https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows_rate.sql
--     Each record displays tv_shows.title - rating sum
--     Results sorted in descending order by the rating
--     useS only one SELECT statement

SELECT title, SUM(rate) AS rating
FROM tv_show_ratings, tv_shows
WHERE tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;
