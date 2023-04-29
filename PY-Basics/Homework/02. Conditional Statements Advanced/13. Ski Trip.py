days_ofc = int(input())
room = input()
grade = input()

price = 0
days = days_ofc - 1

if room == 'room for one person':
    price = days * 18.00
    if grade == 'positive':
        price += price * 0.25
        print(f'{price:.2f}')
    elif grade == 'negative':
        price -= price * 0.1
        print(f'{price:.2f}')

elif room == 'apartment':
    if days < 10:
        price = days * 25.00
        if grade == 'positive':
            price += price * 0.25
            price -= price * 0.3
            print(f'{price:.2f}')
        elif grade == 'negative':
            price -= price * 0.1
            price -= price * 0.3
            print(f'{price:.2f}')

    elif 15 >= days >= 10:
        price = days * 25.00
        if grade == 'positive':
            price += price * 0.25
            price -= price * 0.35
            print(f'{price:.2f}')
        elif grade == 'negative':
            price -= price * 0.1
            price -= price * 0.35
            print(f'{price:.2f}')

    elif days > 15:
        price = days * 25.00
        if grade == 'positive':
            price += price * 0.25
            price -= price * 0.5
            print(f'{price:.2f}')
        elif grade == 'negative':
            price -= price * 0.1
            price -= price * 0.5
            print(f'{price:.2f}')

elif room == 'president apartment':
    if days < 10:
        price = days * 35.00
        if grade == 'positive':
            price += price * 0.25
            price -= price * 0.1
            print(f'{price:.2f}')
        elif grade == 'negative':
            price -= price * 0.1
            price -= price * 0.1
            print(f'{price:.2f}')

    elif 15 >= days >= 10:
        price = days * 35.00
        if grade == 'positive':
            price += price * 0.25
            price -= price * 0.15
            print(f'{price:.2f}')
        elif grade == 'negative':
            price -= price * 0.1
            price -= price * 0.15
            print(f'{price:.2f}')

    elif days > 15:
        price = days * 35.00
        if grade == 'positive':
            price += price * 0.25
            price -= price * 0.2
            print(f'{price:.2f}')
        elif grade == 'negative':
            price -= price * 0.1
            price -= price * 0.2
            print(f'{price:.2f}')

