from classes import *

def create_room(name, size, fee):
    return Room(name, size, fee)
def create_guest_profile(name, cash, fave_song):
    return Guest(name, cash, fave_song)
def create_song(name, artist, genre, length):
    return Song(name, artist, genre, length)

song_master_list = []
room_master_list = []

def add_song_to_master_list(name, artist, genre, length):
    name = create_song(name, artist, genre, length)
    song_master_list.append(name)

def add_room_to_master_list(name, size, fee):
    name = create_room(name, size, fee)
    room_master_list.append(name)