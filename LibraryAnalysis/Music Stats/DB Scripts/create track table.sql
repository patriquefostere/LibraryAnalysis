create table Tracks
(
	TrackId int identity(1,1) not null Primary Key,
	TrackPath varchar(255),
	AlbumId int Foreign Key References Albums(AlbumId)
	-- 2nd foreign key allowed?
	ArtistId int Foreign Key References Artists(ArtistId)
)