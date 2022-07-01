class Room:
    def __init__(self, _name):
        self.name = _name
        self.guests = []
        self.songs = []
    
    def check_in(self, guest):
        self.guests.append(guest)
    
    def check_out(self, guest):
        pass

    def find_guest_by_name(self, guest_name):
        for guest in self.guests:
            if guest.name == guest_name:
                return guest
        return 'Guest Not Found'
