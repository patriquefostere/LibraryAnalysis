import json
from StringHelper import EscapeApostrophes
import Queries

def GetArtistInsertQuery(artistName, classDictionary):
    insertLine = 'insert into Artists (ArtistName, ArtistPath)' 
    valuesLine = f"values ('{artistName}','{classDictionary[artistName].path}')"

    return insertLine + valuesLine

def GetAlbumInsertQuery(albumName, albumPath, artistId):
    insertLine = 'insert into Albums (AlbumName, AlbumPath, ArtistId) ' 
    
    valuesLine = f"values ('{albumName}','{albumPath}',{artistId})"

    return insertLine + valuesLine

def GetTrackInsertQuery(trackName, trackPath, albumId, artistId):
    insertLine = 'insert into Tracks(TrackName, TrackPath, AlbumId, ArtistId) '

    valuesLine = f"values ('{trackName}','{trackPath}',{albumId},{artistId})"

    return insertLine + valuesLine

def GetExistsQuery(tableName, uniqueKey, value):
    return f"SELECT 1 FROM {tableName} WHERE {uniqueKey} = '{value}'"

def GetTrackDetailsInsertQuery(trackDetails, trackId):
    insertLine = 'insert into TrackDetails(LastAccessed, DatesAccessedSerialized, TrackId) '

    lastAccessed = ConvertStringDateToSqlDateTime(trackDetails.lastAccessed)
    datesAccessed = json.dumps([trackDetails.lastAccessed])  

    valuesLine = f"values ({lastAccessed},'{datesAccessed}',{trackId})"

    return insertLine + valuesLine

# 01/12/2023 14:18 -> 20231201 14:18
def ConvertStringDateToSqlDateTime(date):
    dateAndTime = date.split(' ')
    date = dateAndTime[0]
    time = dateAndTime[1]
    dayMonthYear = date.split('/')
    day = dayMonthYear[0]
    month = dayMonthYear[1]
    year = dayMonthYear[2]

    return f"'{year}{month}{day} {time}'"

def GetTrackDetailsUpdateQuery(trackDetails, trackId):
    updateLine = 'update TrackDetails '

    updatedDatesAccessedSerialized = UpdateDatesAccessedSerialized(trackDetails, trackId)

    setLine = f"set LastAccessed = {ConvertStringDateToSqlDateTime(trackDetails.lastAccessed)}, DatesAccessedSerialized = '{EscapeApostrophes(updatedDatesAccessedSerialized)}' "

    whereLine = f'where TrackId = {trackId}'

    return updateLine + setLine + whereLine

# this will probably need some work 
# - converting dates
def UpdateDatesAccessedSerialized(trackDetails, trackId):
    datesAccessedSerialized = Queries.GetTrackDetails(trackId)[1]

    tempJson = json.dumps(datesAccessedSerialized)

    # issue with how datesAccessed is saved?
    #  - stops being a json format?
    datesAccessedArray = json.loads(datesAccessedSerialized)

    if not str(trackDetails.lastAccessed) in datesAccessedSerialized:
        # datesAccessed does not contain trackDetails.lastAccessed,
        # so datesAccessed needs to be  updated with trackDetails.lastAccessed

        # newDatesAccessed = json.loads(datesAccessed)
        datesAccessedArray.append(trackDetails.lastAccessed)

    
    # convert back to json    
    return json.dumps(datesAccessedArray)
        




