import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("Hold On")
    
    def test_song_has_name(self):
        self.assertEqual("Hold On", self.song.name)