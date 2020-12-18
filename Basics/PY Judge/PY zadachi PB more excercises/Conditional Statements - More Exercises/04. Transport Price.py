n = int(input())
day_or_night = input()

price = 0

if n < 20:
    if day_or_night == 'day':
        price = (0.79 * n) + 0.70
    elif day_or_night == 'night':
        price = (0.90 * n) + 0.70

elif 20 <= n < 100:
    price = 0.09 * n

elif n >= 100:
    price = 0.06 * n

print(f'{price:.2f}')