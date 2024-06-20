-- Get data dump from tvshows.sql file
-- List all shows that have one genre linked frm tvshows table
-- Use INNER JOIN: retrieves data between tables when there's a match
-- Should display title - genre.id both in ASC order
USE DATABASE hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;