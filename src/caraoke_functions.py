from classes import *

def create_room(name, size, fee):
    return Room(name, size, fee)
def create_guest_profile(name, cash):
    return Guest(name, cash)
def create_song(name):
    return Song(name)