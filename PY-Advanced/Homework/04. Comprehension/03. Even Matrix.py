rows = int(input())
result = []
[result.append([]) for _ in range(rows)]

for i in range(rows):
    [result[i].append(int(number)) for number in input().split(", ") if int(number) % 2 == 0]

print(result)
