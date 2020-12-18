import math
number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cacti = int(input())
gift_price = float(input())

magnolia = 3.25 * number_of_magnolias
hyacinth = 4 * number_of_hyacinths
rose = 3.50 * number_of_roses
cactus = 8 * number_of_cacti

total = magnolia + hyacinth + rose + cactus
total -= total * 0.05

if total >= gift_price:
    print(f'She is left with {math.floor(total - gift_price)} leva.')
elif total < gift_price:
    print(f'She will have to borrow {math.ceil(gift_price - total)} leva.')