
class Room:

    def __init__(self, name, capacity, price):
        self.name = name
        self.capacity = capacity
        self.price = price 
        self.songs = []
        self.guests = []

    def guest_check_in(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
        else:
            return "Not enough space in the room, choose another"

    def guest_check_out(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def guest_can_afford_room(self, room_price, guest_cash):
        if room_price <= guest_cash:
            return True 
        else:
            return False 

    def song_in_room(self, guest):
        for song in self.songs:
            if guest.fav_song == song.title:
                return "Yeeahhh"
        else:
            None




    