delete from trackDetails
delete from tracks
delete from albums 
delete from artists

DBCC CHECKIDENT (N'TrackDetails', RESEED, 0);
DBCC CHECKIDENT (N'Tracks', RESEED, 0);
DBCC CHECKIDENT (N'Albums', RESEED, 0);
DBCC CHECKIDENT (N'Artists', RESEED, 0);