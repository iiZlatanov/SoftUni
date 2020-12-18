flower_type = input()
flower_number = int(input())
budget = int(input())

price = 0

if flower_type == 'Roses':
    price = 5 * flower_number
elif flower_type == 'Dahlias':
    price = 3.80 * flower_number
elif flower_type == 'Tulips':
    price = 2.80 * flower_number
elif flower_type == 'Narcissus':
    price = 3 * flower_number
elif flower_type == 'Gladiolus':
    price = 2.50 * flower_number

if flower_type == 'Roses' and flower_number > 80:
    price -= price * 0.1
elif flower_type == 'Dahlias' and flower_number > 90:
    price -= price * 0.15
elif flower_type == 'Tulips' and flower_number > 80:
    price -= price * 0.15
elif flower_type == 'Narcissus' and flower_number < 120:
    price += price * 0.15
elif flower_type == 'Gladiolus' and flower_number < 80:
    price += price * 0.2

calc = abs(price - budget)
if price <= budget:
    print(f'Hey, you have a great garden with {flower_number} {flower_type} and {calc:.2f} leva left.')
elif price > budget:
    print(f'Not enough money, you need {calc:.2f} leva more.')