strawberry_price = float(input())
bananas_in_kgs = float(input())
oranges_in_kgs = float(input())
raspberries_in_kgs = float(input())
strawberries_in_kgs = float(input())

price_for_strawberries = strawberry_price * strawberries_in_kgs
price_for_raspberries = (strawberry_price / 2) * raspberries_in_kgs
raspberries_for_oranges_calculations = (strawberry_price / 2) - (strawberry_price / 2 * 0.4)
price_for_oranges = raspberries_for_oranges_calculations * oranges_in_kgs
raspberries_for_bananas_calculations = (strawberry_price / 2) - (strawberry_price / 2 * 0.8)
price_for_bananas = raspberries_for_bananas_calculations * bananas_in_kgs

total = price_for_strawberries + price_for_bananas + price_for_oranges + price_for_raspberries
print(total)