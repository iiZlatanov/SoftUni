from project.dvd import DVD
from typing import List


class Customer:
    def __init__(self, name: str, age: int, id: int) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds: List[DVD] = []

    def __repr__(self) -> str:
        return f"{self.id}: {self.name} of age {self.age} " \
               f"has {len(self.rented_dvds)} " \
               f"rented DVD's ({', '.join([dvd.name for dvd in self.rented_dvds])})"
