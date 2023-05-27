# def grocery_store(**kwargs):
#     sorted_products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
#     result = ""
#     for product, quantity in sorted_products:
#         result += f"{product}: {quantity}\n"
#
#     return result

def grocery_store(**kwargs):
    sorted_products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return "\n".join(f"{p}: {q}" for p, q in sorted_products)


# def grocery_store(**kwargs):
#     return "\n".join(f"{p}: {q}" for p, q in sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
print(grocery_store( bread=5, pasta=12, eggs=12,
))

print(grocery_store( bread=2, pasta=2, eggs=20, carrot=1,
))
