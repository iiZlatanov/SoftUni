from collections import deque

quantity_of_food = int(input())
data = deque(map(int, input().split()))

print(max(data))

while True:
    if len(data) > 0 and data[0] < quantity_of_food:
        quantity_of_food -= data[0]
        data.popleft()
    elif len(data) > 0 and data[0] > quantity_of_food:
        print(f"Orders left: {' '.join(list(map(str, data)))}")
        break
    else:
        print("Orders complete")
        break
