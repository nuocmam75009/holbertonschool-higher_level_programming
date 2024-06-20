-- From database hbtn_0d_tvshows
-- List all shows without a genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows.tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_show_genres.id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;