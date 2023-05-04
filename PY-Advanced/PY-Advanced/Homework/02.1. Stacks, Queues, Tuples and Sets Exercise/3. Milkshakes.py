from collections import deque
from copy import copy
chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))
milkshakes_counter = 0

for el in copy(chocolates):
    if el <= 0:
        chocolates.remove(el)
for el in copy(cups_of_milk):
    if el <= 0:
        cups_of_milk.remove(el)
if len(chocolates) > 0 and len(cups_of_milk) > 0:
    while True:
        if chocolates[-1] == cups_of_milk[0]:
            chocolates.pop()
            cups_of_milk.popleft()
            milkshakes_counter += 1
        else:
            cups_of_milk.append(cups_of_milk.popleft())
            chocolates[-1] -= 5
            if chocolates[-1] <= 0:
                chocolates.pop()
        if milkshakes_counter == 5 or len(chocolates) == 0 or len(cups_of_milk) == 0:
            break


if milkshakes_counter == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(el) for el in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(el) for el in cups_of_milk)}")
else:
    print("Milk: empty")
