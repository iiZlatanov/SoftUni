items = input().split("|")
budget = float(input())
list_with_new_prices = []
total = 0
profit = 0

for pair in items:
    support_list = pair.split("->")
    for item in support_list:
        price_of_item = 1000000000000000000
        if item == "Clothes" or item == "Accessories" or item == "Shoes":
            type_of_item = item
        if item != "Clothes" and item != "Accessories" and item != "Shoes":
            price_of_item = float(item)
        if type_of_item == "Clothes" and price_of_item <= 50.00 or type_of_item == "Shoes" and price_of_item <= 35.00 or type_of_item == "Accessories" and price_of_item <= 20.50:
            if budget >= price_of_item:
                budget -= price_of_item
                list_with_new_prices.append(price_of_item + price_of_item * 0.4)
                total += price_of_item + price_of_item * 0.4
                profit += price_of_item * 0.4

total += budget
for member in list_with_new_prices:
    print("%.2f" % member, end=" ")
print("")
print(f"Profit: {profit:.2f}")
if total >= 150:
    print("Hello, France!")
else:
    print("Time to go.")