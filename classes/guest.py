class Guest:
    def __init__(self, _name, _cash, _fave_song):
        self.name = _name
        self.cash = _cash
        self.fave_song = _fave_song
    
    def reduce_cash(self, amount_change):
        self.cash -= amount_change
    def check_fave_song(self, song_name):
        if self.fave_song == song_name:
            return "Whooo!"