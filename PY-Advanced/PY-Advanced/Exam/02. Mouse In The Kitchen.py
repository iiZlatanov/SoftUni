ROWS,COLS = [int(x) for x in input().split(",")]
cupboard_area = [[ch for ch in input()] for _ in range(ROWS)]
cheese_counter = 0
max_cheese = 0

for i in range(ROWS):
        for j in range(COLS):
            if cupboard_area[i][j] == "C":
                max_cheese += 1
            elif cupboard_area[i][j] == "M":
                mouse_coordinates = [i, j]
                cupboard_area[i][j] = "*"

command = input()
while True:
    if command == "up":
        mouse_coordinates[0] -= 1
        if mouse_coordinates[0] < 0 or mouse_coordinates[0] == ROWS or mouse_coordinates[1] < 0 or mouse_coordinates[1] == COLS:
            cupboard_area[mouse_coordinates[0] + 1][mouse_coordinates[1]] = "M"
            print("No more cheese for tonight!")
            break
        else:
            if cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] == "@":
                mouse_coordinates[0] += 1
            elif cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] == "C":
                cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "*"
                cheese_counter += 1
                if cheese_counter == max_cheese:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "M"
                    break
            elif cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] == "T":
                print("Mouse is trapped!")
                cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "M"
                break


    elif command == "down":
        mouse_coordinates[0] += 1
        if mouse_coordinates[0] < 0 or mouse_coordinates[0] == ROWS or mouse_coordinates[1] < 0 or mouse_coordinates[1] == COLS:
            cupboard_area[mouse_coordinates[0] - 1][mouse_coordinates[1]] = "M"
            print("No more cheese for tonight!")
            break
        else:
            if cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] == "@":
                mouse_coordinates[0] -= 1
            elif cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] == "C":
                cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "*"
                cheese_counter += 1
                if cheese_counter == max_cheese:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "M"
                    break
            elif cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] == "T":
                print("Mouse is trapped!")
                cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "M"
                break

    elif command == "left":
        mouse_coordinates[1] -= 1
        if mouse_coordinates[0] < 0 or mouse_coordinates[0] == ROWS or mouse_coordinates[1] < 0 or mouse_coordinates[1] == COLS:
            cupboard_area[mouse_coordinates[0]][mouse_coordinates[1] + 1] = "M"
            print("No more cheese for tonight!")
            break
        else:
            if cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] == "@":
                mouse_coordinates[1] += 1
            elif cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] == "C":
                cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "*"
                cheese_counter += 1
                if cheese_counter == max_cheese:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "M"
                    break
            elif cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] == "T":
                print("Mouse is trapped!")
                cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "M"
                break

    elif command == "right":
        mouse_coordinates[1] += 1
        if mouse_coordinates[0] < 0 or mouse_coordinates[0] == ROWS or mouse_coordinates[1] < 0 or mouse_coordinates[1] == COLS:
            cupboard_area[mouse_coordinates[0]][mouse_coordinates[1] - 1] = "M"
            print("No more cheese for tonight!")
            break
        else:
            if cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] == "@":
                mouse_coordinates[1] -= 1
            elif cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] == "C":
                cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "*"
                cheese_counter += 1
                if cheese_counter == max_cheese:
                    print("Happy mouse! All the cheese is eaten, good night!")
                    cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "M"
                    break
            elif cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] == "T":
                print("Mouse is trapped!")
                cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "M"
                break
    elif command == "danger":
        cupboard_area[mouse_coordinates[0]][mouse_coordinates[1]] = "M"
        print("Mouse will come back later!")
        break
    command = input()

for row in cupboard_area:
        print("".join(row))
