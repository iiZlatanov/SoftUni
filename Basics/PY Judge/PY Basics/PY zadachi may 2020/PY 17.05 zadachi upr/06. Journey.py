budget = float(input())
season = input()

destination = 0
rest_type = 0
price = 0

if budget <= 100:
    destination = 'Bulgaria'
elif 100 < budget <= 1000:
    destination = 'Balkans'
elif budget > 1000:
    destination = 'Europe'

if destination == 'Europe':
    rest_type = 'Hotel'
    price = budget * 0.9
    print('Somewhere in Europe')
    print(f'{rest_type} - {price:.2f} ')
elif destination == 'Bulgaria':
    if season == 'summer':
        rest_type = 'Camp'
        price = budget * 0.3
        print('Somewhere in Bulgaria')
        print(f'{rest_type} - {price:.2f} ')
    elif season == 'winter':
        rest_type = 'Hotel'
        price = budget * 0.7
        print('Somewhere in Bulgaria')
        print(f'{rest_type} - {price:.2f} ')
elif destination == 'Balkans':
    if season == 'summer':
        rest_type = 'Camp'
        price = budget * 0.4
        print('Somewhere in Balkans')
        print(f'{rest_type} - {price:.2f} ')
    elif season == 'winter':
        rest_type = 'Hotel'
        price = budget * 0.8
        print('Somewhere in Balkans')
        print(f'{rest_type} - {price:.2f} ')