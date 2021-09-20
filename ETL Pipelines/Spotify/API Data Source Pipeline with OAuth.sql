CREATE TABLE RecentlyReleasedAlbums (
	id VARCHAR(60),
	album VARCHAR(150),
	album_type VARCHAR(30),
	release_date DATE,
	total_tracks INT,
	total_artists INT
)

CREATE TABLE RecentlyReleasedArtists (
	id VARCHAR(60),
	artist VARCHAR(80),
	artist_type VARCHAR(30)
)

SELECT * FROM RecentlyReleasedAlbums
SELECT * FROM RecentlyReleasedArtists