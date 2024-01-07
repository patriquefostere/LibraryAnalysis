create table TrackDetails
(
	DetailId int identity(1,1) not null Primary Key,
	LastAccessed DateTime,
	DatesAccessedSerialized varchar(2047),
	PlaysCount int,
	TrackId int Foreign Key References Tracks(TrackId)
)