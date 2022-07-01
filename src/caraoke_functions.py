from classes import *

def create_room(name, size, fee):
    return Room(name, size, fee)
def create_guest_profile(name, cash, fave_song):
    return Guest(name, cash, fave_song)
def create_song(name):
    return Song(name)