CREATE PROCEDURE sp_Albums_Released 
(	
	@date DATE, 
	@tracks INT OUTPUT
)
AS
BEGIN
	SELECT * 
	FROM RecentlyReleasedAlbums
	WHERE release_date=@date
END

SELECT * FROM RecentlyReleasedAlbums

DECLARE @track INT
EXEC sp_Albums_Released '2021-09-17', @track OUTPUT
SELECT @track
