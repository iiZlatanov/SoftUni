from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit, Seed


class Mouse(Mammal):
    @property
    def food_that_eats(self) -> list:
        return [Fruit, Vegetable]

    @property
    def gain_weight(self) -> float:
        return 0.10

    def make_sound(self) -> str:
        return "Squeak"


class Dog(Mammal):
    @property
    def food_that_eats(self) -> list:
        return [Meat]

    @property
    def gain_weight(self) -> float:
        return 0.40

    def make_sound(self) -> str:
        return "Woof!"


class Cat(Mammal):
    @property
    def food_that_eats(self) -> list:
        return [Meat, Vegetable]

    @property
    def gain_weight(self) -> float:
        return 0.30

    @property
    def make_sound(self) -> str:
        return "Meow"


class Tiger(Mammal):
    @property
    def food_that_eats(self) -> list:
        return [Meat]

    @property
    def gain_weight(self) -> float:
        return 1.00

    def make_sound(self) -> str:
        return "ROAR!!!"
