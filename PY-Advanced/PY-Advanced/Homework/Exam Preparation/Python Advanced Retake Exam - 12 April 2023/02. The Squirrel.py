field_size = int(input())
commands_data = input().split(", ")
field = [[ch for ch in input()] for _ in range(field_size)]
hazelnuts_collected = 0

for i in range(field_size):
    for j in range(field_size):
        if field[i][j] == "s":
            squirrel_position_x_coord = i
            squirrel_position_y_coord = j
flag = True

for command in commands_data:
    if command == "up":
        squirrel_position_x_coord -= 1
    elif command == "down":
        squirrel_position_x_coord += 1
    elif command == "left":
        squirrel_position_y_coord -= 1
    elif command == "right":
        squirrel_position_y_coord += 1

    if 0 > squirrel_position_x_coord or squirrel_position_x_coord == field_size or 0 > squirrel_position_y_coord or squirrel_position_y_coord == field_size:#We are out of the matrix scope in this situation
        print("The squirrel is out of the field.")
        flag = False
        break
    elif field[squirrel_position_x_coord][squirrel_position_y_coord] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        flag = False
        break
    elif field[squirrel_position_x_coord][squirrel_position_y_coord] == "h":
        field[squirrel_position_x_coord][squirrel_position_y_coord] = "*"
        hazelnuts_collected += 1
        if hazelnuts_collected == 3:
            print("Good job! You have collected all hazelnuts!")
            flag = False
            break

if flag:
    print("There are more hazelnuts to collect.")
print(f"Hazelnuts collected: {hazelnuts_collected}")
