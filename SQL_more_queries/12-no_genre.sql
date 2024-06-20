-- From database hbtn_0d_tvshows
-- List all shows without a genre
SELECT tv_shows.title COALESCE(tv_show_genres.genre_id, -1) AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genre.tv_show_id
-- WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, genre_id ASC;