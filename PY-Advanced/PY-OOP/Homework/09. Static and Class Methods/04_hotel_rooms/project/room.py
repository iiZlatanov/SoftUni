class Room:
    def __init__(self, number: int, capacity: int) -> None:

        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people: int) -> None or str:
        if self.is_taken or people > self.capacity:
            return f"Room number {self.number} cannot be taken"

        self.guests = people
        self.is_taken = True

    def free_room(self) -> None or str:
        if not self.is_taken:
            return f"Room number {self.number} is not taken"

        self.guests = 0
        self.is_taken = False
