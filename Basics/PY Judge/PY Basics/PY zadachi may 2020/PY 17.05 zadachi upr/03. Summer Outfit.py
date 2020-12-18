degrees = int(input())
time_of_day = input()

shirt = 'Shirt'
t_shirt = 'T-Shirt'
moccasins = 'Moccasins'
sandals = 'Sandals'
swim_suit = 'Swim Suit'
barefoot = 'Barefoot'
sneakers = 'Sneakers'
sweatshirt = 'Sweatshirt'


if time_of_day == 'Morning':
    if 10 <= degrees <= 18:
        print(f"It's {degrees} degrees, get your {sweatshirt} and {sneakers}.")
    elif 18 < degrees <= 24:
        print(f"It's {degrees} degrees, get your {shirt} and {moccasins}.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your {t_shirt} and {sandals}.")

elif time_of_day == 'Afternoon':
    if 10 <= degrees <= 18:
        print(f"It's {degrees} degrees, get your {shirt} and {moccasins}.")
    elif 18 < degrees <= 24:
        print(f"It's {degrees} degrees, get your {t_shirt} and {sandals}.")
    elif degrees >= 25:
        print(f"It's {degrees} degrees, get your {swim_suit} and {barefoot}.")
elif time_of_day == 'Evening':
    print(f"It's {degrees} degrees, get your {shirt} and {moccasins}.")
