create table Albums
(
	AlbumId int IDENTITY (1,1) NOT NULL Primary Key,
	AlbumName varchar(255),
	AlbumPath varchar(255),
	ArtistId int Foreign Key References Artists(ArtistId)
)