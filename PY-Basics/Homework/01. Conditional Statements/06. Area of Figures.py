from math import pi

type_of_geometric_figure = str(input())

if type_of_geometric_figure == 'square':
    length_of_one_side = float(input())
    volume_of_the_square = length_of_one_side ** 2
    print(f'{volume_of_the_square:.3f}')
elif type_of_geometric_figure == 'rectangle':
    length_of_side_one = float(input())
    length_of_side_two = float(input())
    volume_of_the_rectangle = length_of_side_one * length_of_side_two
    print(f'{volume_of_the_rectangle:.3f}')
elif type_of_geometric_figure == 'circle':
    radius_of_the_circle = float(input())
    volume_of_the_circle = (radius_of_the_circle ** 2) * pi
    print(f'{volume_of_the_circle:.3f}')
elif type_of_geometric_figure == 'triangle':
    length_of_side = float(input())
    length_of_height_of_side = float(input())
    volume_of_the_triangle = length_of_side * length_of_height_of_side / 2
    print(f'{volume_of_the_triangle:.3f}')
