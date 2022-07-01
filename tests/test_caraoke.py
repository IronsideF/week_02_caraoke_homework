import unittest
from classes import *
from src.caraoke_functions import *

class TestCaraoke(unittest.TestCase):

    def test_create_room(self):
        room1 = create_room("The Freddie Mercury Room", 8, 5)
        self.assertEqual("The Freddie Mercury Room", room1.name)
        self.assertEqual(8, room1.size)
        self.assertEqual(5, room1.entry_fee)
    def test_create_guest_profile(self):
        guest1 = create_guest_profile("Rachel", 100)
        self.assertEqual("Rachel", guest1.name)
        self.assertEqual(100, guest1.cash)
    def test_create_song(self):
        song1 = create_song("Hold On")
        self.assertEqual("Hold On", song1.name)
