from collections import deque

SIZE_ROWS_AND_COLS = 6
field = [input().split() for _ in range(6)]
commands_list = deque(input().split(", "))

found_deposits = {
    "water": False,
    "metal": False,
    "concrete": False
}

for i in range(SIZE_ROWS_AND_COLS):
    for j in range(SIZE_ROWS_AND_COLS):
        if field[i][j] == "E":
            rover_coords = [i, j]
            break

while commands_list:
    command = commands_list.popleft()

    if command == "left":
        rover_coords[1] -= 1
        if rover_coords[1] == -1:
            rover_coords[1] = 5
    elif command == "right":
        rover_coords[1] += 1
        if rover_coords[1] == 6:
            rover_coords[1] = 0
    elif command == "up":
        rover_coords[0] -= 1
        if rover_coords[0] == -1:
            rover_coords[0] = 5
    elif command == "down":
        rover_coords[0] += 1
        if rover_coords[0] == 6:
            rover_coords[0] = 0

    if field[rover_coords[0]][rover_coords[1]] == "W":
        print(f"Water deposit found at ({rover_coords[0]}, {rover_coords[1]})")
        found_deposits["water"] = True
        field[rover_coords[0]][rover_coords[1]] = "-"
    elif field[rover_coords[0]][rover_coords[1]] == "M":
        print(f"Metal deposit found at ({rover_coords[0]}, {rover_coords[1]})")
        found_deposits["metal"] = True
        field[rover_coords[0]][rover_coords[1]] = "-"
    elif field[rover_coords[0]][rover_coords[1]] == "C":
        print(f"Concrete deposit found at ({rover_coords[0]}, {rover_coords[1]})")
        found_deposits["concrete"] = True
        field[rover_coords[0]][rover_coords[1]] = "-"
    elif field[rover_coords[0]][rover_coords[1]] == "R":
        print(f"Rover got broken at ({rover_coords[0]}, {rover_coords[1]})")
        break

if all([found_deposits["water"], found_deposits["metal"], found_deposits["concrete"]]):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
