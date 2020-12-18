city = input()
s = float(input())

commission = 0

if city == 'Sofia':
    if 0 <= s <= 500:
        commission = s * 0.05
        print(f'{commission:.2f}')
    elif 500 <= s <= 1000:
        commission = s * 0.07
        print(f'{commission:.2f}')
    elif 1000 <= s <= 10000:
        commission = s * 0.08
        print(f'{commission:.2f}')
    elif 10000 < s:
        commission = s * 0.12
        print(f'{commission:.2f}')

elif city == 'Varna':
    if 0 <= s <= 500:
        commission = s * 0.045
        print(f'{commission:.2f}')
    elif 500 <= s <= 1000:
        commission = s * 0.075
        print(f'{commission:.2f}')
    elif 1000 <= s <= 10000:
        commission = s * 0.1
        print(f'{commission:.2f}')
    elif 10000 < s:
        commission = s * 0.13
        print(f'{commission:.2f}')

elif city == 'Plovdiv':
    if 0 <= s <= 500:
        commission = s * 0.055
        print(f'{commission:.2f}')
    elif 500 <= s <= 1000:
        commission = s * 0.08
        print(f'{commission:.2f}')
    elif 1000 <= s <= 10000:
        commission = s * 0.12
        print(f'{commission:.2f}')
    elif 10000 < s:
        commission = s * 0.145
        print(f'{commission:.2f}')

if commission == 0:
    print('error')
