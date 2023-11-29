from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        for room in self.rooms:
            if room_number == room.number:
                room.take_room(people)
                self.guests = room.guests

    def free_room(self, room_number: int):
        for room in self.rooms:
            if room_number == room.number:
                room.free_room()
                self.guests = 0

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        total_guests = sum([r.guests for r in self.rooms])

        return f"Hotel {self.name} has {total_guests} total guests\nFree rooms: {', '.join(free_rooms)}\nTaken rooms: {', '.join(taken_rooms)}"
