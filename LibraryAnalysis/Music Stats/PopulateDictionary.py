import os
from win32com.client import Dispatch
from Artist import Artist
from Album import Album
from Track import Track
from TrackDetails import TrackDetails
from StringHelper import EscapeApostrophes

rootPath = r'C:\Users\foste\Desktop\Music'
    
def Ignore(compareString, fileType = None):
    ignores = ["ini", "jpg", "cue", "txt", "png", "log"]

    for ignore in ignores:
        if ignore in compareString.lower() or (fileType != None and ignore in fileType.lower()): return True

    return False

def GetTracks(albumPath):
    shell = Dispatch("Shell.Application")
    ns = shell.NameSpace(albumPath)
    albumContents = ns.Items()

    tracks = {}
    for item in albumContents:
        trackName = EscapeApostrophes(item)
        if not Ignore(trackName, item.Type):

            # strange thing: path is passed in as a string, but self.path is a tuple 
            # self.path = (path,)

            trackPath = os.path.join(albumPath, trackName) # string here
            lastAccessed = ns.GetDetailsOf(item,5)
            trackDetails = TrackDetails(lastAccessed)
            tracks[trackName] = Track(trackName, trackPath, trackDetails) # trackPath is still a string
            # but now, tracks[trackName].path is a tuple?!
            # tracks[trackName].path = (trackPath,) somehow - so we have to access it with [0]

            # tracks[trackName].path = GetTrackPath(tracks[trackName]) # not using the ctor seems to fix it
            tracks[trackName].path = EscapeApostrophes(trackPath) # not using the ctor seems to fix it
            tracks[trackName].title = EscapeApostrophes(trackName)

    return tracks

def GetAlbums(albums, artistPath):
    result = {}
    for albumName in albums:
        if Ignore(albumName): continue

        albumPath = os.path.join(artistPath, albumName) #rootPath/A/ABBA/voulez vous

        tracks = GetTracks(albumPath)
        result[EscapeApostrophes(albumName)] = Album(albumName, albumPath, tracks)

    return result
            
def PopulateClassDictionary():
    # letters = os.listdir(rootPath)
    # letters.pop()# remove __Management entry, may need to specify by "__Management"
    letters = ['A']

    # data on artists/albums/tracks/properties as classes
    classDictionary =  {}

    for letter in letters:# loop over A-Z
        artistsBeginningWithLetter = os.path.join(rootPath, letter)#rootPath/A/ABBA

        artistsBeginningWithLetterDirs = os.listdir(artistsBeginningWithLetter)

        for artistName in artistsBeginningWithLetterDirs:
            artistPath = os.path.join(artistsBeginningWithLetter, artistName) #rootPath/A/ABBA

            albums = []

            try:
                albums = os.listdir(artistPath)
            except:
                print(artistPath, " not a valid path")
                continue
            
            # pp.pprint(albums)# this exposes lots of bad elements, eg .jpgs, .inis

            actualAlbums = GetAlbums(albums, artistPath)

            artist = Artist(artistName, artistPath, actualAlbums)
            classDictionary[artistName] = artist

    return classDictionary


def PopulateTextDictionary(classDictionary):
    # data on artists/albums/tracks/properties in pure text
    textDictionary = {} 

    for artistName in classDictionary:
        textDictionary[artistName] = {}

        for albumName in classDictionary[artistName].albums:
            # textDictionary[artistName][albumName] = []
            textDictionary[artistName][albumName] = {}
            for trackName in classDictionary[artistName].albums[albumName].tracks:
                
                # textDictionary[artistName][albumName].append(trackName)
                currentTrack = classDictionary[artistName].albums[albumName].tracks[trackName]
                textDictionary[artistName][albumName][trackName] = PopulateTextDetails(currentTrack.trackDetails)

    return textDictionary

def PopulateTextDetails(trackDetails):
    return {
        "date accessed" : trackDetails.lastAccessed,
        "dates_accessed" : trackDetails.datesAccessed
    }

