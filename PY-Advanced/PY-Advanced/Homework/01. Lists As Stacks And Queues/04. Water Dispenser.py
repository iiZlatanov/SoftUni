from collections import deque

current_quantity = int(input())
names_in_queue = deque()
data = input()

while data != "Start":
    names_in_queue.append(data)
    data = input()

data = input()
while data != "End":
    if len(data) > 7:
        water = data.split()
        current_quantity += int(water[1])
    else:
        data = int(data)
        if data <= current_quantity:
            current_quantity -= data
            print(f"{names_in_queue[0]} got water")
            names_in_queue.popleft()
        else:
            print(f"{names_in_queue[0]} must wait")
            names_in_queue.popleft()
    data = input()

print(f"{current_quantity} liters left")
