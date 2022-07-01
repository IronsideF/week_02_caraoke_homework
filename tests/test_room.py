import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("The Freddie Mercury Room")
        self.guest1 = Guest("Rachel")
        self.guest2 = Guest("Lauren")
        self.guest3 = Guest("Derrian")
        self.song1 = Song("Hold On")
        self.song2 = Song("Foundations")
        self.song3 = Song("Shake It Off")
    
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
        # guest_in_room = self.room.find_guest_by_name("Rachel")
        self.assertEqual(self.guest1, self.room.find_guest_by_name("Rachel"))
    def test_room_can_find_guest_not_found(self):
        self.assertEqual('Guest Not Found', self.room.find_guest_by_name("Rachel"))
