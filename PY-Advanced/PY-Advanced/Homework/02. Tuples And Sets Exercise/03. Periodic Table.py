n = int(input())
result = []

for _ in range(n):
    data = input().split()
    for el in data:
        result.append(el)

print("\n".join(set(result)))
