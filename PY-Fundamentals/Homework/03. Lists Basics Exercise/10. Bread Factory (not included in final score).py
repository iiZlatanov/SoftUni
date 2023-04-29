order = input().split("|")
energy = 100
coins = 100
flag = False

for element in order:
    event, value = element.split("-")
    value = int(value)

    if event == "rest":
        if energy == 100:
            print("You gained 0 energy.")
        elif energy < 100:
            side_calculations = 100 - energy
            if value <= side_calculations:
                energy += value
                print(f"You gained {value} energy.")
            elif value > side_calculations:
                energy += side_calculations
                print(f"You gained {side_calculations} energy.")
        print(f"Current energy: {energy}.")

    elif event == 'order':
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            print("You had to rest!")
            energy += 50

    else:
        if coins > value:
            print(f"You bought {event}.")
            coins -= value
        else:
            print(f"Closed! Cannot afford {event}.")
            flag = True

    if flag is True:
        break

if flag is False:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")