budget = int(input())
season = input()
fisher_numbers = int(input())

if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600

if fisher_numbers <= 6:
    price -= price * 0.1
elif 7 <= fisher_numbers <= 11:
    price -= price * 0.15
elif 11 < fisher_numbers:
    price -= price * 0.25

if fisher_numbers % 2 == 0 and season != 'Autumn':
    price -= price * 0.05

if budget >= price:
    print(f'Yes! You have {budget - price:.2f} leva left.')
elif budget < price:
    print(f'Not enough money! You need {price - budget:.2f} leva.')
