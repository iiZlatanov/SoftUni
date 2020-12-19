month = input()
number_of_sleepovers = int(input())

apartment = 0
studio = 0

if month == 'May' or month == 'October':
    apartment = 65 * number_of_sleepovers
    studio = 50 * number_of_sleepovers
    if 14 >= number_of_sleepovers > 7:
        studio -= studio * 0.05
    elif number_of_sleepovers > 14:
        studio -= studio * 0.3
        apartment -= apartment * 0.1

elif month == 'June' or month == 'September':
    apartment = 68.70 * number_of_sleepovers
    studio = 75.20 * number_of_sleepovers
    if number_of_sleepovers > 14:
        apartment -= apartment * 0.1
        studio -= studio * 0.2

elif month == 'July' or month == 'August':
    apartment = 77 * number_of_sleepovers
    studio = 76 * number_of_sleepovers
    if number_of_sleepovers > 14:
        apartment -= apartment * 0.1

print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')