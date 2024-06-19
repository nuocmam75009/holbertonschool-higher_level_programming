-- Get data dump from tvshows.sql file
-- List all shows that have one genre linked frm tvshows table
-- Should display title - genre.id both in ASC order
USE hbtn_0d_tvshows.sql;
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC