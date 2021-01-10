data = input()
products_and_quantities = {}
total_quantity = 0

while data != "statistics":
    data_list = data.split(": ")
    if data_list[0] in products_and_quantities:
        products_and_quantities[data_list[0]] += int(data_list[1])
    else:
        products_and_quantities[data_list[0]] = int(data_list[1])
    data = input()

for values in products_and_quantities.values():
    total_quantity += values
print("Products in stock:")
for product, quantity in products_and_quantities.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products_and_quantities)}\nTotal Quantity: {total_quantity}")
