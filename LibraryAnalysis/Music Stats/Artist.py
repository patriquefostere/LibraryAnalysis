from StringHelper import EscapeApostrophes

class Artist:
    def __init__(self, name, path, albums):
        self.name = EscapeApostrophes(name)
        self.path = EscapeApostrophes(path)
        self.albums = albums


    