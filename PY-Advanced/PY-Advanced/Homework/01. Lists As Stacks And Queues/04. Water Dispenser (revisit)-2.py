from collections import deque

current_quantity = int(input())
names = deque()

while True:
    command = input()

    if command == "Start":
        break
    names.append(command)

while True:
    command = input()

    if command == "End":
        print(f"{current_quantity} liters left")
        break

    data = command.split()
    if data[0] == "refill":
        current_quantity += int(data[1])
    else:
        if int(data[0]) <= current_quantity:
            print(f"{names.popleft()} got water")
            current_quantity -= int(data[0])
        else:
            print(f"{names.popleft()} must wait")
