people_in_queue = int(input())
MAX_PEOPLE_PER_WAGON = 4

flag = False
index = 0
wagons_state = [int(x) for x in input().split()]

for wagon in wagons_state:
    while wagon < 4:
        if people_in_queue > 0:
            wagon += 1
            people_in_queue -= 1
        else:
            wagons_state[index] = wagon
            flag = True
            break
    if flag:
        break

    wagons_state[index] = wagon
    index += 1

if flag and wagons_state[-1] != 4:
    print("The lift has empty spots!")
else:
    print(f"There isn't enough space! {people_in_queue} people in a queue!")

print(*wagons_state)
