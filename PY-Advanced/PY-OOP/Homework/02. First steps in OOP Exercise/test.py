class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 0.01


ivan = Person("Ivan", 1.83)
ivan.grow()
print(ivan.height)
