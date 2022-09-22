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
    elif len(data) > 7:# you can also use .startswith("refill")((ili da se napravi konstanta s string refill vytre i da se polzva elif data.startswith(konstantata v koqto ima refill kato string)))
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
