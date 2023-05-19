MATRIX_SIZE = int(input())
racing_number = input()
race_route = [input().split() for data in range(MATRIX_SIZE)]
x, y = [0, 0]
distance_covered = 0
flag = True
tunnels_coordinates = []


def no_more_tunnels():
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            if race_route[i][j] == "T":
                race_route[i][j] = "."


for k in range(MATRIX_SIZE):
    for l in range(MATRIX_SIZE):
        if race_route[k][l] == "T":
            tunnels_coordinates.append([k, l])

while True:
    command = input()
    if command == "End":
        race_route[x][y] = "C"
        print(f"Racing car {racing_number} DNF.")
        flag = False
        break

    elif command == "up":
        x -= 1
        if race_route[x][y] == ".":
            distance_covered += 10
        else:
            if race_route[x][y] == "F":
                race_route[x][y] = "C"
                distance_covered += 10
                break
            elif race_route[x][y] == "T":
                tunnels_coordinates.remove([x, y])
                x, y = tunnels_coordinates[0]
                no_more_tunnels()
                distance_covered += 30

    elif command == "down":
        x += 1
        if race_route[x][y] == ".":
            distance_covered += 10
        else:
            if race_route[x][y] == "F":
                race_route[x][y] = "C"
                distance_covered += 10
                break
            elif race_route[x][y] == "T":
                tunnels_coordinates.remove([x, y])
                x, y = tunnels_coordinates[0]
                no_more_tunnels()
                distance_covered += 30

    elif command == "left":
        y -= 1
        if race_route[x][y] == ".":
            distance_covered += 10
        else:
            if race_route[x][y] == "F":
                race_route[x][y] = "C"
                distance_covered += 10
                break
            elif race_route[x][y] == "T":
                tunnels_coordinates.remove([x, y])
                x, y = tunnels_coordinates[0]
                no_more_tunnels()
                distance_covered += 30

    elif command == "right":
        y += 1
        if race_route[x][y] == ".":
            distance_covered += 10
        else:
            if race_route[x][y] == "F":
                race_route[x][y] = "C"
                distance_covered += 10
                break
            elif race_route[x][y] == "T":
                tunnels_coordinates.remove([x, y])
                x, y = tunnels_coordinates[0]
                no_more_tunnels()
                distance_covered += 30

if flag is True:
    print(f"Racing car {racing_number} finished the stage!")
print(f"Distance covered {distance_covered} km.")
for el in race_route:
    print("".join(el))
