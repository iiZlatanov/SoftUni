field_size = int(input())
matrix_data = [input().split() for _ in range(field_size)]
traps_coordinates = []
directions = {
    "up": 0,
    "down": 0,
    "left": 0,
    "right": 0,
}
right_coords = []
left_coords = []
up_coords = []
down_coords = []

for x in range(field_size):
    for y in range(field_size):
        if matrix_data[x][y] == "B":
            starting_coordinates = (x, y)
        elif matrix_data[x][y] == "X":
            traps_coordinates.append((x, y))

x_coord = starting_coordinates[0]
y_coord = starting_coordinates[1]
while True:
    x_coord -= 1
    if x_coord >= 0:
        if matrix_data[x_coord][y_coord] == "X":
            break
        elif matrix_data[x_coord][y_coord].isdigit():
            directions["up"] += int(matrix_data[x_coord][y_coord])
            up_coords.append([x_coord , y_coord])
    else:
        break

x_coord = starting_coordinates[0]
y_coord = starting_coordinates[1]
while True:
    x_coord += 1
    if x_coord <= field_size - 1:
        if matrix_data[x_coord][y_coord] == "X":
            break
        elif matrix_data[x_coord][y_coord].isdigit():
            directions["down"] += int(matrix_data[x_coord][y_coord])
            down_coords.append([x_coord, y_coord])
    else:
        break

x_coord = starting_coordinates[0]
y_coord = starting_coordinates[1]
while True:
    y_coord -= 1
    if y_coord >= 0:
        if matrix_data[x_coord][y_coord] == "X":
            break
        elif matrix_data[x_coord][y_coord].isdigit():
            directions["left"] += int(matrix_data[x_coord][y_coord])
            left_coords.append([x_coord, y_coord])
    else:
        break

x_coord = starting_coordinates[0]
y_coord = starting_coordinates[1]
while True:
    y_coord += 1
    if y_coord <= field_size - 1:
        if matrix_data[x_coord][y_coord] == "X":
            break
        elif matrix_data[x_coord][y_coord].isdigit():
            directions["right"] += int(matrix_data[x_coord][y_coord])
            right_coords.append([x_coord, y_coord])
    else:
        break

max_value = 0
key_of_max_value = ""
for key,value in directions.items():
    if value > max_value:
        max_value = value
        key_of_max_value = key

print(key_of_max_value)
if key_of_max_value == "up":
    print(*up_coords, sep="\n")
elif key_of_max_value == "down":
    print(*down_coords, sep="\n")
elif key_of_max_value == "left":
    print(*left_coords, sep="\n")
elif key_of_max_value == "right":
    print(*right_coords, sep="\n")
print(max_value)
