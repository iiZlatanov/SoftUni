class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def increase_age(self):
        pass

    @staticmethod
    def calc_two_nums(a, b):
        return a + b
