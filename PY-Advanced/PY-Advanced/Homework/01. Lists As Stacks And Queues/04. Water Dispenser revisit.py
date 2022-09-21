from collections import deque

quantity_of_water = int(input())
current_queue = deque()

data = input()
while data != "Start":
    current_queue.append(data)
    data = input()
data = input()

while True:
    if data == "End":
        print(f"{quantity_of_water} liters left")
        break
    elif len(data) > 7:
        water = data.split()
        quantity_of_water += int(water[1])
        data = input()
    else:
        requested_water = int(data)
        if requested_water <= quantity_of_water:
            quantity_of_water -= requested_water
            print(f"{current_queue.popleft()} got water")
        else:
            print(f"{current_queue.popleft()} must wait")
        data = input()
