from collections import deque

food_quantity = int(input())
orders_data = deque([int(_) for _ in input().split()]) #Using map - orders_data = list(map(int, input().split()))
print(max(orders_data))

while len(orders_data) > 0:
    if food_quantity >= orders_data[0]:
        food_quantity -= orders_data[0]
        orders_data.popleft()
    else:
        print(f"Orders left: " + " ".join(list(map(str, orders_data))))
        break
    if len(orders_data) == 0:
        print("Orders complete")
        break
