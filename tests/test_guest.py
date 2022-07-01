import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Rachel", 100, "Hold On")

    def test_guest_has_name(self):
        self.assertEqual("Rachel", self.guest.name)
    def test_guest_has_cash(self):
        self.assertEqual(100, self.guest.cash)
    def test_guest_has_favourite_song(self):
        self.assertEqual("Hold On", self.guest.fave_song)
    