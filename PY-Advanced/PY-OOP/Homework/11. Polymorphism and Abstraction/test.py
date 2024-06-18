class Triangle:
    def get_perimeter(self):
        return "Triangle perimeter"


class Square:
    def get_perimeter(self):
        return "Square perimeter"


class Rhombus:
    def get_perimeter(self):
        return "Rhombus perimeter"


class New_Shape:
    def get_perimeter(self):
        return "New Shape perimeter"


shapes = [Triangle(), Square(), Rhombus(), New_Shape()]
for shape in shapes:
    print(shape.get_perimeter())
