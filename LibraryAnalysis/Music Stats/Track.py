from StringHelper import EscapeApostrophes

class Track:
    def __init__(self, title, path, trackDetails):
        self.title = EscapeApostrophes(title) # name of track
        self.path = EscapeApostrophes(path), # path to track

        # strange thing: path is passed in as a string, but self.path is a tuple 
        # self.path = (path,)
        # solution: set path twice, the second time like "currentTrack.path = newPath"

        self.trackDetails = trackDetails #  this is a TrackDetails object which contains lastAccessed


    

    
