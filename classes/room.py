class Room:
    def __init__(self, _name, _size, _fee):
        self.name = _name
        self.guests = []
        self.songs = []
        self.size = _size
        self.entry_fee = _fee
        self.bar_tab = 0
    
    def check_in(self, guest):
        if len(self.guests) < self.size and guest.cash >= self.entry_fee:
            self.guests.append(guest)
            guest.reduce_cash(self.entry_fee)
            if self.find_song_by_name(guest.fave_song) in self.songs:
                return guest.check_fave_song(guest.fave_song)
        elif len(self.guests) >= self.size:
            return 'This room is full'
        elif guest.cash < self.entry_fee:
            return 'Not enough money'

    def find_guest_by_name(self, guest_name):
        for guest in self.guests:
            if guest.name == guest_name:
                return guest
        return 'Guest Not Found'

    def check_out(self, guest_name):
        guest = self.find_guest_by_name(guest_name)
        if guest != 'Guest Not Found':
            self.guests.remove(guest)
        else:
            return "That Guest is not in this room"
    
    def add_song_to_room(self, song):
        self.songs.append(song)
    
    def find_song_by_name(self, song_name):
        for song in self.songs:
            if song.name == song_name:
                return song
    
    def add_to_tab(self, amount_change):
        self.bar_tab += amount_change

    def check_in_on_tab(self, guest):
        if len(self.guests) < self.size:
            self.guests.append(guest)
            self.add_to_tab(self.entry_fee)
            if self.find_song_by_name(guest.fave_song) in self.songs:
                return guest.check_fave_song(guest.fave_song)
        elif len(self.guests) >= self.size:
            return 'This room is full'