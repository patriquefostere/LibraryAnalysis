import QueryBuilder
from StringHelper import EscapeApostrophes
from TrackDetails import TrackDetailsResult
from DbHelper import DoInsertOrUpdate, DoFetch
import Queries

def WriteClassDictionaryToDb(classDictionary):# possibly should combine this with PopulateClassDictionary?
    for artistName in classDictionary:

        artistExistsQuery = QueryBuilder.GetExistsQuery("Artists", "ArtistName", artistName)
        artistExistsResult = DoFetch(artistExistsQuery)

        if len(artistExistsResult) == 0:
            # insert into artists table
            artistInsertQuery = QueryBuilder.GetArtistInsertQuery(artistName, classDictionary)
            DoInsertOrUpdate(artistInsertQuery)

        for albumName in classDictionary[artistName].albums:

            albumPath = EscapeApostrophes(classDictionary[artistName].albums[albumName].path)
            # need to sanitise because the path is saved to db with ' replaced with ''
            # this is stored in db with single quotes and then retrieved with single quotes            

            albumExistsQuery = QueryBuilder.GetExistsQuery("Albums", "AlbumPath", albumPath)# possibly should albumPath instead of albumName
            albumExistsResult = DoFetch(albumExistsQuery)

            artistId = Queries.GetArtistId(artistName)

            if len(albumExistsResult) == 0:
                #insert into albums table
                albumInsertQuery = QueryBuilder.GetAlbumInsertQuery(albumName, 
                                                                    albumPath, artistId)
                DoInsertOrUpdate(albumInsertQuery)

            for trackName in classDictionary[artistName].albums[albumName].tracks:
                
                trackPath = classDictionary[artistName].albums[albumName].tracks[trackName].path

                trackExistsQuery = QueryBuilder.GetExistsQuery("Tracks", "TrackPath", trackPath)
                trackExistsResult = DoFetch(trackExistsQuery)

                if len(trackExistsResult) == 0:
                    # insert into tracks table
                    albumId = Queries.GetAlbumId(albumName)
                    trackInsertQuery = QueryBuilder.GetTrackInsertQuery(trackName, trackPath, albumId, artistId)
                    DoInsertOrUpdate(trackInsertQuery)
               
                trackDetails = classDictionary[artistName].albums[albumName].tracks[trackName].trackDetails
                # insert into trackDetails table
                trackId = Queries.GetTrackId(trackName)
                UpdateOrInsertIntoTrackDetailsTable(trackId, trackDetails)                

# here we use albumName and artistName because you could have two albums with exact same title
def GetAlbumPath(albumName, artistName):
    artistid = Queries.GetArtistId(artistName)

    query = f"select albumpath from albums where albumname = '{albumName}' and artistid = {artistid}"

    result = DoFetch(query)

    return [0][0]

def UpdateOrInsertIntoTrackDetailsTable(trackId, trackDetails):
    # if exists record with trackId then update, else insert
    existsQuery = QueryBuilder.GetExistsQuery("TrackDetails", "TrackId", trackId)
    existsResult = DoFetch(existsQuery)

    query = ""

    if(len(existsResult) == 1):
        # do update
        query = QueryBuilder.GetTrackDetailsUpdateQuery(trackDetails, trackId)
    else:
        # do insert
        query = QueryBuilder.GetTrackDetailsInsertQuery(trackDetails, trackId)

    DoInsertOrUpdate(query)

