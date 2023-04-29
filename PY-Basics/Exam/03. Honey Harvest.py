flower_type = input()
flower_number = int(input())
season = input()
total = 0


if season == 'Spring':
    if flower_type == 'Sunflower':
        total = flower_number * 10
    elif flower_type == 'Daisy':
        total = flower_number * 12
        total += total * 0.1
    elif flower_type == 'Lavender':
        total = flower_number * 12
    elif flower_type == 'Mint':
        total = flower_number * 10
        total += total * 0.1

elif season == 'Summer':
    if flower_type == 'Sunflower':
        total = flower_number * 8
    elif flower_type == 'Daisy':
        total = flower_number * 8
    elif flower_type == 'Lavender':
        total = flower_number * 8
    elif flower_type == 'Mint':
        total = flower_number * 12
    total += total * 0.1

elif season == 'Autumn':
    if flower_type == 'Sunflower':
        total = flower_number * 12
    elif flower_type == 'Daisy':
        total = flower_number * 6
    elif flower_type == 'Lavender':
        total = flower_number * 6
    elif flower_type == 'Mint':
        total = flower_number * 6
    total -= total * 0.05

print(f'Total honey harvested: {total:.2f}')