product_data, quantity_data = input(), int(input())


def total_price_of_an_order(product: str, quantity: int):
    result = None
    if product == "coffee":
        result = quantity * 1.5
    elif product == "water":
        result = quantity * 1.0
    elif product == "coke":
        result = quantity * 1.4
    elif product == "snacks":
        result = quantity * 2.0

    return result


print(f"{total_price_of_an_order(product_data, quantity_data):.2f}")
