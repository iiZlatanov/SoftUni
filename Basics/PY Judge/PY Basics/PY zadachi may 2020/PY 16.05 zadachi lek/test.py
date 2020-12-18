name_of_product = input()
name_of_town = input()
quantity_of_product = int(input())

coffee_for_sofia = 0.50
coffee_for_plovdiv = 0.40
coffee_for_varna = 0.45
water_for_sofia = 0.80
water_for_plovdiv = 0.70
water_for_varna = 0.70
beer_for_sofia = 1.20
beer_for_plovdiv = 1.15
beer_for_varna = 1.10
sweets_for_sofia = 1.45
sweets_for_plovdiv = 1.30
sweets_for_varna = 1.35
peanuts_for_sofia = 1.60
peanuts_for_plovdiv = 1.50
peanuts_for_varna = 1.55

if name_of_town == 'Sofia' or name_of_town == 'sofia' or 'Sofiq' or 'sofiq':
    if name_of_product == 'coffee':
        print(f'Your total is {quantity_of_product * coffee_for_sofia:.2f} levs.')
    elif name_of_product == 'water':
        print(f'Your total is {quantity_of_product * water_for_sofia:.2f} levs.')
    elif name_of_product == 'beer':
        print(f'Your total is {quantity_of_product * beer_for_sofia:.2f} levs.')
    elif name_of_product == 'sweets':
        print(f'Your total is {quantity_of_product * sweets_for_sofia:.2f} levs.')
    elif name_of_product == 'peanuts':
        print(f'Your total is {quantity_of_product * peanuts_for_sofia:.2f} levs.')
    else:
        print('Please select a product from the list.')
elif name_of_town == 'Plovdiv':
    if name_of_product == 'coffee':
        print(f'Your total is {quantity_of_product * coffee_for_plovdiv:.2f} levs.')
    elif name_of_product == 'water':
        print(f'Your total is {quantity_of_product * water_for_plovdiv:.2f} levs.')
    elif name_of_product == 'beer':
        print(f'Your total is {quantity_of_product * beer_for_plovdiv:.2f} levs.')
    elif name_of_product == 'sweets':
        print(f'Your total is {quantity_of_product * sweets_for_plovdiv:.2f} levs.')
    elif name_of_product == 'peanuts':
        print(f'Your total is {quantity_of_product * peanuts_for_plovdiv:.2f} levs.')
    else:
        print('Please select a product from the list.')
elif name_of_town == 'Varna':
    if name_of_product == 'coffee':
        print(f'Your total is {quantity_of_product * coffee_for_varna:.2f} levs.')
    elif name_of_product == 'water':
        print(f'Your total is {quantity_of_product * water_for_varna:.2f} levs.')
    elif name_of_product == 'beer':
        print(f'Your total is {quantity_of_product * beer_for_varna:.2f} levs.')
    elif name_of_product == 'sweets':
        print(f'Your total is {quantity_of_product * sweets_for_varna:.2f} levs.')
    elif name_of_product == 'peanuts':
        print(f'Your total is {quantity_of_product * peanuts_for_varna:.2f} levs.')
    else:
        print('Please select a product from the list.')
else:
    print('Please choose a city from the list : Sofia, Plovdiv or Varna!')