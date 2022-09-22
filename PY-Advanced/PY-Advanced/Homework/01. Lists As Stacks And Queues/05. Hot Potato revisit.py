kids_data = input().split()
DOOM_COUNTER = int(input())
current_index = -1

while len(kids_data) != 1:
    additional_counter = DOOM_COUNTER
    while additional_counter > 0:
        additional_counter -= 1
        if current_index < DOOM_COUNTER and current_index < (len(kids_data) - 1):
            current_index += 1
        else:
            current_index = 0

    print(f"Removed {kids_data.pop(current_index)}")
    current_index -= 1

print(f"Last is {kids_data[0]}")
