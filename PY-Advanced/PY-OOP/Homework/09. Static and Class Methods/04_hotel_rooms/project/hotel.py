from typing import List, TypeVar, Type
from project.room import Room

T = TypeVar("T", bound="TrivialClass")


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int) -> T:
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        room = [r for r in self.rooms if r.number == room_number][0]
        res = room.take_room(people)
        if not res:
            self.guests += people

    def free_room(self, room_number: int) -> None:
        room = [r for r in self.rooms if r.number == room_number][0]
        guests_count = self.guests
        res = room.free_room()
        if not res:
            self.guests -= guests_count

    def status(self) -> str:
        free_rooms = [r for r in self.rooms if not r.is_taken]
        taken_rooms = [r for r in self.rooms if r.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(r.number) for r in free_rooms])}\n" \
               f"Taken rooms: {', '.join([str(r.number) for r in taken_rooms])}"
