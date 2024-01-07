create table Artists
(
	ArtistId int IDENTITY (1,1) NOT NULL Primary Key,
	ArtistName varchar(255) not null unique,
	ArtistPath varchar(255) not null unique
)

create table Albums
(
	AlbumId int IDENTITY (1,1) NOT NULL Primary Key,
	AlbumName varchar(255) not null unique,
	AlbumPath varchar(255) not null unique,
	ArtistId int Foreign Key References Artists(ArtistId)
)

create table Tracks
(
	TrackId int identity(1,1) not null Primary Key,
	TrackPath varchar(255) not null unique,
	TrackName varchar(255) not null,
	AlbumId int Foreign Key References Albums(AlbumId),
	ArtistId int Foreign Key References Artists(ArtistId) 
)

create table TrackDetails
(
	DetailId int identity(1,1) not null Primary Key,
	LastAccessed DateTime,
	DatesAccessedSerialized varchar(2047),
	TrackId int Foreign Key References Tracks(TrackId) not null unique
)