n1 = int(input())
n2 = int(input())
operator = input()

result = 0
percentage = 0
if n2 == 0:
    print(f'Cannot divide {n1} by zero')
elif operator == '-':
    result = n1 - n2
    even_or_odd = result % 2
    if even_or_odd != 0:
        percentage = 'odd'
        print(f'{n1} {operator} {n2} = {result} - {percentage}')
    elif even_or_odd == 0:
        percentage = 'even'
        print(f'{n1} {operator} {n2} = {result} - {percentage}')

elif operator == '+':
    result = n1 + n2
    even_or_odd = result % 2
    if even_or_odd != 0:
        percentage = 'odd'
        print(f'{n1} {operator} {n2} = {result} - {percentage}')
    elif even_or_odd == 0:
        percentage = 'even'
        print(f'{n1} {operator} {n2} = {result} - {percentage}')

elif operator == '*':
    result = n1 * n2
    even_or_odd = result % 2
    if even_or_odd != 0:
        percentage = 'odd'
        print(f'{n1} {operator} {n2} = {result} - {percentage}')
    elif even_or_odd == 0:
        percentage = 'even'
        print(f'{n1} {operator} {n2} = {result} - {percentage}')

elif operator == '/':
    result = n1 / n2
    print(f'{n1} / {n2} = {result:.2f}')

elif operator == '%':
    result = n1 % n2
    print(f'{n1} % {n2} = {result}')