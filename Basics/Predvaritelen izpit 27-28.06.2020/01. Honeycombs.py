import math
number_of_bees = int(input())
number_of_flowers = int(input())

total = number_of_bees * number_of_flowers * 0.21

honeycombs_filled = total // 100
honey_left = total % 100

print(f'{math.floor(honeycombs_filled)} honeycombs filled.')
print(f'{honey_left:.2f} grams of honey left.')