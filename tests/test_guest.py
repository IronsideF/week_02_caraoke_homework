import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Rachel", 100)

    def test_guest_has_name(self):
        self.assertEqual("Rachel", self.guest.name)
    def test_guest_has_cash(self):
        self.assertEqual(100, self.guest.cash)
    