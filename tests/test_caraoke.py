import unittest
from classes import *
from src.caraoke_functions import *

class TestCaraoke(unittest.TestCase):

    def test_create_room(self):
        room1 = create_room("The Freddie Mercury Room")
        self.assertEqual("The Freddie Mercury Room", room1.name)
    def test_create_guest_profile(self):
        guest1 = create_guest_profile("Rachel")
        self.assertEqual("Rachel", guest1.name)
    def test_create_song(self):
        song1 = create_song("Hold On")
        self.assertEqual("Hold On", song1.name)
