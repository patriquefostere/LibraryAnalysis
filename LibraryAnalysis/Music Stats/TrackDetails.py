class TrackDetails:
    def __init__(self, lastAccessed):
        self.lastAccessed = lastAccessed

class TrackDetailsResult:
    def __init__(self, lastAccessed, datesAccessedSerialized):
        self.lastAccessed = lastAccessed
        self.datesAccessedSerialized = datesAccessedSerialized