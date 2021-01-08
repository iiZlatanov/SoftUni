command = input()
price_without_taxes = 0
taxes = 0

while command != "regular" and command != "special":
    prices = float(command)
    if prices > 0:
        price_without_taxes += prices
        taxes += prices * 0.2
    elif prices <= 0:
        print("Invalid price!")

    command = input()

total_price = price_without_taxes + taxes
if command == "regular":
    if price_without_taxes == 0:
        print("Invalid order!")
    else:
        print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {price_without_taxes:.2f}$\n"
              f"Taxes: {taxes:.2f}$\n-----------\nTotal price: {total_price:.2f}$")
elif command == "special":
    if price_without_taxes == 0:
        print("Invalid order!")
    else:
        print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {price_without_taxes:.2f}$\n"
              f"Taxes: {taxes:.2f}$\n-----------\nTotal price: {total_price - total_price * 0.1:.2f}$")
