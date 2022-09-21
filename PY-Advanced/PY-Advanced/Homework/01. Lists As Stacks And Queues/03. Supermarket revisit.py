from collections import deque

END_COMMAND = "End"
PAID_COMMAND = "Paid"
data = input()
customers_names = deque()

while True:
    if data != PAID_COMMAND and data != END_COMMAND:
        customers_names.append(data)

    elif data == PAID_COMMAND:
        print("\n".join(customers_names))
        while customers_names:
            customers_names.popleft()

    elif data == END_COMMAND:
        print(f"{len(customers_names)} people remaining.")
        break
    data = input()
