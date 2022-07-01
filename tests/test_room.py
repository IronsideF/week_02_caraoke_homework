import unittest
from classes.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("The Freddie Mercury Room")
    
    def test_roo_has_name(self):
        self.assertEqual("The Freddie Mercury Room", self.room1.name)