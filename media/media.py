class Media():
    """Media object abstraction"""
    def __init__(self, name, sinopsis, poster, trailer):
        self.name = name
        self.sinopsis = sinopsis
        self.poster = poster
        self.trailer = trailer

class Movie(Media):
    """Concrete class for movies"""
    def __init__(self, name, sinopsis, poster, trailer, duration, year):
        Media.__init__(self, name, sinopsis, poster, trailer)
        self.duration = duration
        self.year = year

class Serie(Media):
    """Concrete class for TV Serie"""
    def __init__(self, name, sinopsis, poster, trailer, seasons, tv):
        Media.__init__(self, name, sinopsis, poster, trailer)
        self.seasons = seasons
        self.tv = tv
        
