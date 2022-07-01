import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("The Freddie Mercury Room", 2, 5)
        self.guest1 = Guest("Rachel", 100, "Hold On")
        self.guest2 = Guest("Lauren", 50, "Foundations")
        self.guest3 = Guest("Derrian", 500, "Shake It Off")
        self.song1 = Song("Hold On")
        self.song2 = Song("Foundations")
        self.song3 = Song("Shake It Off")
        self.song_list = [self.song1, self.song2, self.song3]
    
    def test_room_has_name(self):
        self.assertEqual("The Freddie Mercury Room", self.room.name)
    def test_room_has_guests(self):
        self.assertEqual(0, len(self.room.guests))
    def test_room_has_songs(self):
        self.assertEqual(0, len(self.room.songs))
    def test_check_in_adds_guests(self):
        self.room.check_in(self.guest1)
        self.assertEqual(1, len(self.room.guests))
    def test_room_can_find_guest(self):
        self.room.check_in(self.guest1)
        self.assertEqual(self.guest1, self.room.find_guest_by_name("Rachel"))
    def test_room_can_find_guest_not_found(self):
        self.assertEqual('Guest Not Found', self.room.find_guest_by_name("Rachel"))
    def test_check_out_removes_guests(self):
        self.room.check_in(self.guest1)
        self.room.check_out("Rachel")
        self.assertEqual(0, len(self.room.guests))
    def test_check_out_guest_not_found(self):
        self.assertEqual("That Guest is not in this room", self.room.check_out("Rachel"))
    def test_add_song(self):
        self.room.add_song_to_room(self.song1)
        self.assertEqual(1, len(self.room.songs))
    def test_room_has_size(self):
        self.assertEqual(2, self.room.size)
    def test_room_cannot_add_too_many_guests(self):
        self.room.check_in(self.guest1)
        self.room.check_in(self.guest2)
        self.assertEqual("This room is full", self.room.check_in(self.guest3))
    def test_room_has_fee(self):
        self.assertEqual(5, self.room.entry_fee)
    def test_room_fee_applied(self):
        self.room.check_in(self.guest1)
        self.assertEqual(self.guest1.cash, 95)
    def test_room_fee_prevents_entry(self):
        self.guest1.cash = 0
        self.assertEqual('Not enough money', self.room.check_in(self.guest1))
    def test_guest_fave_song_check_in(self):
        self.room.songs = self.song_list
        self.assertEqual("Whooo!", self.room.check_in(self.guest1))
    def test_guest_fave_song_not_present(self):
        self.assertEqual(None, self.room.check_in(self.guest1))
    def test_room_has_tab(self):
        self.assertEqual(0, self.room.bar_tab)
    def test_add_to_tab(self):
        self.room.add_to_tab(5)
        self.assertEqual(5, self.room.bar_tab)
    def test_check_in_adds_to_tab(self):
        self.room.check_in_on_tab(self.guest1)
        self.assertEqual(5, self.room.bar_tab)


