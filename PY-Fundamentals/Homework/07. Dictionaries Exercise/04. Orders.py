command = input()
product_dict = {}

while command != "buy":
    product_price_quantity_list = command.split()
    product = product_price_quantity_list[0]
    price = float(product_price_quantity_list[1])
    quantity = int(product_price_quantity_list[2])
    if product not in product_dict:
        product_dict[product] = [price, quantity]
    else:
        product_dict[product][0] = price
        product_dict[product][1] += quantity
    command = input()

for key, value in product_dict.items():
    product_dict[key] = value[0] * value[1]
    print(f"{key} -> {product_dict[key]:.2f}")
