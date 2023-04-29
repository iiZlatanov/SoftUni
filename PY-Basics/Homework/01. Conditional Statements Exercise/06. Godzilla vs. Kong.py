budget = float(input())
number_of_extras = int(input())
price_per_extra_clothing = float(input())

decor_price = budget * 0.1

if number_of_extras > 150:
    price_per_extra_clothing = price_per_extra_clothing - (price_per_extra_clothing * 0.1)

money_needed = (number_of_extras * price_per_extra_clothing) + decor_price

if money_needed > budget:
    print('Not enough money!')
    print(f'Wingard needs {(money_needed - budget):.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {(budget - money_needed):.2f} leva left.')