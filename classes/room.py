class Room:
    def __init__(self, _name):
        self.name = _name
        self.guests = []
        self.songs = []
    
    def check_in(self, guest):
        self.guests.append(guest)

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