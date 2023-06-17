from collections import deque

integers_list = [int(x) for x in input().split()]
AVERAGE = sum(integers_list) / len(integers_list)
bigger_than_average_list = []
result = []

for num in integers_list:
    if num > AVERAGE:
        bigger_than_average_list.append(num)

if bigger_than_average_list:
    sorted_nums_list = deque(sorted(bigger_than_average_list, reverse=True))
    while sorted_nums_list and len(result) != 5:
        result.append(sorted_nums_list.popleft())
    print(*result)
else:
    print("No")
