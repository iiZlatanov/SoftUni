open_tabs_in_browser = int(input())
salary = float(input())

for i in range(1, open_tabs_in_browser+1):
    name_of_website = str(input())
    if name_of_website == 'Facebook':
        salary -= 150
    if name_of_website == 'Instagram':
        salary -= 100
    if name_of_website == 'Reddit':
        salary -= 50
    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(f'{salary:.0f}')