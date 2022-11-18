import unittest 

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):

        self.guest1 = Guest("Jake", "Jamming", 100)
        self.guest2 = Guest("Anna", "I will survive", 80)
        self.guest3 = Guest("Paul", "Takin' my time", 10)
    
        self.room1 = Room("Pop", 2, 20)
        self.room2 = Room("Rock", 3, 30)
        self.room3 = Room("Reggae", 2, 40)

        self.song1 = Song("Jamming")
        self.song2 = Song("Taking' my time")
        self.song3 = Song("Stand by me")
    
    def test_room_has_a_name(self):
        self.assertEqual("Pop", self.room1.name)

    def test_room1_capacity(self):
        self.assertEqual(2, self.room1.capacity)

    def test_guest_has_a_name(self):
        self.assertEqual("Jake", self.guest1.name)

    def test_guest_has_a_fav_song(self):
        self.assertEqual("Jamming", self.guest1.fav_song)
    
    def test_song_has_a_title(self):
        self.assertEqual("Jamming", self.song1.title)
    
    def test_guest_can_check_in_room(self):
        self.room1.guest_check_in(self.guest1)
        self.assertEqual(1, len(self.room1.guests))

    def test_guest_can_check_out_from_room(self):
        self.room1.guest_check_in(self.guest1)
        self.room1.guest_check_out(self.guest1)
        self.assertEqual(0, len(self.room1.guests))

    def test_room_is_full(self):
        self.room1.guest_check_in(self.guest1)
        self.room1.guest_check_in(self.guest2)
        self.room1.guest_check_in(self.guest3)
        self.assertEqual(2, len(self.room1.guests))
    
    def test_can_add_song_to_room(self):
        self.room1.add_song_to_room(self.song1)
        self.assertEqual(1, len(self.room1.songs))

    def test_guest_can_afford_room(self):
        expected_outcome = True
        actual_outcome= self.room1.guest_can_afford_room(self.room1.price, self.guest1.cash)
        self.assertEqual(expected_outcome, actual_outcome)

    def test_guest_can_not_afford_room(self):
        expected_outcome = False
        actual_outcome = self.room1.guest_can_afford_room(self.room1.price, self.guest3.cash)
        self.assertEqual(actual_outcome, expected_outcome)
        
    def test_guest_fav_song_in_room(self):
        self.room1.add_song_to_room(self.song1)
        self.room1.add_song_to_room(self.song2)
        self.room1.add_song_to_room(self.song3)
        expected_outcome = "Yeeahhh"
        actual_outcome = self.room1.song_in_room(self.guest1, self.song1)
        self.assertEqual(expected_outcome, actual_outcome)