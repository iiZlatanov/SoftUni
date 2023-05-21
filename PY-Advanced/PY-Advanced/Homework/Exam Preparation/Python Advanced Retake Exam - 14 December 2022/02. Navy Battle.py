FIELD_SIZE = int(input())
field = [[ch for ch in input()]for _ in range(FIELD_SIZE)]
times_hit_by_a_mine = 0
hit_battle_cruisers = 0
submarine_position = []
flag = True

for i in range(FIELD_SIZE):
    for j in range(FIELD_SIZE):
        if field[i][j] == "S":
            submarine_position = [i, j]
            field[i][j] = "-"

while True:
    command = input()

    if command == "up":
        submarine_position[0] -= 1
    elif command == "down":
        submarine_position[0] += 1
    elif command == "left":
        submarine_position[1] -= 1
    elif command == "right":
        submarine_position[1] += 1

    if field[submarine_position[0]][submarine_position[1]] == "*":
        times_hit_by_a_mine += 1
        field[submarine_position[0]][submarine_position[1]] = "-"
        if times_hit_by_a_mine == 3:
            flag = False
            break
    elif field[submarine_position[0]][submarine_position[1]] == "C":
        hit_battle_cruisers += 1
        field[submarine_position[0]][submarine_position[1]] = "-"
        if hit_battle_cruisers == 3:
            break

field[submarine_position[0]][submarine_position[1]] = "S"
if flag is True:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
else:
    print(f"Mission failed, U-9 disappeared! Last known coordinates {submarine_position}!")

for el in field:
    print("".join(el))
