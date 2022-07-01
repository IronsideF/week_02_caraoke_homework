import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("The Freddie Mercury Room")
    
    def test_room_has_name(self):
        self.assertEqual("The Freddie Mercury Room", self.room1.name)
    def test_room_has_guests(self):
        self.assertEqual(0, len(self.room1.guests))
    def test_room_has_songs(self):
        self.assertEqual(0, len(self.room1.songs))