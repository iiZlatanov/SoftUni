from collections import deque

data = input()
customers = deque()
numbers = 0

while True:
    if data != "Paid" and data != "End":
        customers.append(data)
        numbers += 1

    elif data == "Paid":
        print("\n".join(customers))
        customers = []

    elif data == "End":
        print(f"{len(customers)} people remaining.")
        break
    data = input()
