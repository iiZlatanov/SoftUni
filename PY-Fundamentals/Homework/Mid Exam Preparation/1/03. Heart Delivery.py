hearts_needed_list = list(map(int, input().split("@")))
position_index = 0
command = input()

while command != "Love!":
    new_list = command.split(" ")
    number_of_jumps = new_list[1]
    position_index += int(number_of_jumps)
    if position_index >= len(hearts_needed_list):
        position_index = 0
    if hearts_needed_list[position_index] <= 2:
        if hearts_needed_list[position_index] == 0:
            print(f"Place {position_index} already had Valentine's day.")
        elif hearts_needed_list[position_index] != 0:
            hearts_needed_list[position_index] = 0
            print(f"Place {position_index} has Valentine's day.")
    elif hearts_needed_list[position_index] > 2:
        hearts_needed_list[position_index] -= 2
    command = input()
flag = False
failed_houses_list = []
for element in hearts_needed_list:
    if element != 0:
        failed_houses_list.append(element)
        flag = True

if flag is False:
    print(f"Cupid's last position was {position_index}.")
    print("Mission was successful.")
else:
    print(f"Cupid's last position was {position_index}.")
    print(f"Cupid has failed {len(failed_houses_list)} places.")
