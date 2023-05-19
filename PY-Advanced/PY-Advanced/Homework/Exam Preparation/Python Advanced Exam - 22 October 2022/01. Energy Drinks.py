from collections import deque

MAXIMUM_CAFFEINE = 300
drank_caffeine = 0
caffeine_list = [int(x) for x in input().split(", ")]
energy_drinks = deque(int(x) for x in input().split(", "))

while caffeine_list and energy_drinks:
    current_caffeine = caffeine_list.pop()
    current_energy_drink = energy_drinks.popleft()
    caffeine = current_caffeine * current_energy_drink
    if caffeine + drank_caffeine < 300:
        drank_caffeine += caffeine
    else:
        energy_drinks.append(current_energy_drink)
        drank_caffeine -= 30
        if drank_caffeine < 0:
            drank_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(drink) for drink in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {drank_caffeine} mg caffeine.")
