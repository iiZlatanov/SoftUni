one_square_meter_price = 7.61
how_much_square_meters_are_gonna_be_landscaped = float(input())
price = one_square_meter_price * how_much_square_meters_are_gonna_be_landscaped
discount = price * 0.18
after_discount = price - discount
print(f'The final price is: {after_discount} lv.')
print(f'The discount is: {discount} lv.')