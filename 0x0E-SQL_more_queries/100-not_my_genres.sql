-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

--     The tv_shows table contains only one record where title = Dexter (but the id can be different)
--     Each record displays: tv_genres.name
--     Results sorted in ascending order by the genre name
--     You can use a maximum of two SELECT statement

SELECT tv_genres.name
FROM tv_genres
WHERE name NOT IN
(SELECT tv_genres.name
FROM tv_shows
RIGHT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT OUTER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres
.id WHERE title = "Dexter")
ORDER BY name ASC;

    SELECT tv_genres.name
      FROM tv_genres
     WHERE tv_genres.name NOT IN (
    SELECT tv_genres.name
      FROM tv_genres
INNER JOIN tv_show_genres
        ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
     WHERE tv_shows.title = "Dexter")
  ORDER BY tv_genres.name ASC;
