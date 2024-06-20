-- From database hbtn_0d_tvshows
-- List all shows without a genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
WHERE tv_show_genres.genre_id IS NULL;