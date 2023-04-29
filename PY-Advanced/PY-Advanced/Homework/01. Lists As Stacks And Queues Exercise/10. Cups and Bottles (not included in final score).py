from collections import deque

cups = deque(list(map(int, input().split())))
bottles = [int(_) for _ in input().split()]
wasted_water = 0
bottles_copy = bottles.copy()
cups_copy = cups.copy()
flag = False

while len(bottles_copy) > 0:
    last_bottle = bottles_copy.pop()
    first_cup = cups_copy[0]
    while first_cup > 0:
        first_cup -= last_bottle
        if first_cup < 1:
            cups_copy.popleft()
        else:
            last_bottle = bottles_copy.pop()
    if len(cups_copy) == 0:
        flag = True
        break

if flag is True: #Scenario where cups are gonna be filled
    while len(cups) > 0:
        current_cup = cups.popleft()
        while current_cup > 0:
            current_bottle = bottles.pop()
            current_cup -= current_bottle
            if current_cup < 0:
                wasted_water += -current_cup
    print("Bottles: ", end="")
    while len(bottles) > 0:
        print(bottles[-1], end=" ")
        bottles.pop()
    print(f"\nWasted litters of water: {wasted_water}")

else: #Scenario where cups are NOT gonna be filled
    current_cup_1 = cups[0]
    while len(bottles) > 0:
        current_bottle_1 = bottles.pop()
        current_cup_1 -= current_bottle_1
        if current_cup_1 < 0:
            wasted_water += -current_cup_1
        if current_cup_1 < 1:
            cups.popleft()
            current_cup_1 = cups[0]
    print("Cups: ", end="")
    while len(cups) > 0:
        print(cups[0], end=" ")
        cups.popleft()
    print(f"\nWasted litters of water: {wasted_water}")
