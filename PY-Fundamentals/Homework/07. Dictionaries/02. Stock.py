data = input().split()
customer_data = input().split()
stock_dict = {}

for item in range(0, len(data), 2):
    key = data[item]
    value = int(data[item + 1])
    stock_dict[key] = value
flag = False
for product in customer_data:
        if product in stock_dict:
            print(f"We have {stock_dict[product]} of {product} left")
        else:
            print(f"Sorry, we don't have {product}")
