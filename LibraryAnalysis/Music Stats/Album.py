from StringHelper import EscapeApostrophes

class Album:
    def __init__(self, title, path, tracks):
        self.title = EscapeApostrophes(title)
        self.path = EscapeApostrophes(path)
        self.tracks = tracks