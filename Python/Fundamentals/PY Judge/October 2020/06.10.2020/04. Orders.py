product = input()
quantity = int(input())


def calculating(product, quantity):
    result = None
    if product == "coffee":
        result = quantity * 1.50
    elif product == "water":
        result = quantity * 1.00
    elif product == "coke":
        result = quantity * 1.40
    elif product == "snacks":
        result = quantity * 2.00
    return result


end_result = calculating(product, quantity)
print(f"{end_result:.2f}")