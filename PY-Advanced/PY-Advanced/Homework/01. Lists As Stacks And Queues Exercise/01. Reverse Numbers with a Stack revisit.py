data = input().split()
result_list = []

for _ in range(len(data)):
    result_list.append(data[-1])
    data.pop()

print(" ".join(result_list))
