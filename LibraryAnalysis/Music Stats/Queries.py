from DbHelper import DoFetch

def GetTrackDetails(trackId):
    query = f"select lastaccessed,datesaccessedserialized from trackdetails where trackid = {trackId}"

    return DoFetch(query) [0]

def GetDatesAccessedSerialized(trackId):
    query = f"select DatesAccessedSerialized from TrackDetails where TrackId = {trackId}"
    return DoFetch(query)

def GetArtistId(artistName):
    query = f"select artistid from artists where artistname = '{artistName}'"
    return DoFetch(query)[0][0] # not sure why "[0][0]" is necessary, but it is

def GetAlbumId(albumName):
    query = f"select albumid from albums where albumname = '{albumName}'"
    return DoFetch(query)[0][0]

def GetTrackId(trackName):
    query = f"select trackid from tracks where trackname = '{trackName}'"
    return DoFetch(query)[0][0]
