MATRIX_SIZE = int(input())
matrix = [input().split() for _ in range(MATRIX_SIZE)]
flag = True
tea_collected = 0

for i in range(MATRIX_SIZE):
    for j in range(MATRIX_SIZE):
        if matrix[i][j] == "R":
            rabbit_hole_coordinate = (i, j)
        if matrix[i][j] == "A":
            alice_coordinates = [i, j]

while True:
    command = input()
    matrix[alice_coordinates[0]][alice_coordinates[1]] = "*"

    if command == "up":
        alice_coordinates[0] -= 1
    elif command == "down":
        alice_coordinates[0] += 1
    elif command == "left":
        alice_coordinates[1] -= 1
    elif command == "right":
        alice_coordinates[1] += 1

    if 0 <= alice_coordinates[0] < MATRIX_SIZE and 0 <= alice_coordinates[1] < MATRIX_SIZE:
        if matrix[alice_coordinates[0]][alice_coordinates[1]] == "R":
            matrix[alice_coordinates[0]][alice_coordinates[1]] = "*"
            flag = False
            break
        elif matrix[alice_coordinates[0]][alice_coordinates[1]].isdigit():
            tea_collected += int(matrix[alice_coordinates[0]][alice_coordinates[1]])
            if tea_collected >= 10:
                matrix[alice_coordinates[0]][alice_coordinates[1]] = "*"
                break
    else:
        flag = False
        break

if flag is True:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for el in matrix:
    print(" ".join(el))
