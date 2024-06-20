-- Get data dump from tvshows.sql file
-- List all shows that have one genre linked frm tvshows table
-- Use INNER JOIN: retrieves data between tables when there's a match
-- Should display title - genre.id both in ASC order
-- if a show has no genre display NULL
-- Coalesce function returns first non-null value
USE DATABASE hbtn_0d_tvshows
SELECT tv_shows.title COALESCE (tv_show_genres.genre_id, NULL) AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, genre_id ASC;