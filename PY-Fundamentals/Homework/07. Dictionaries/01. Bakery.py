data = input().split()
bakery = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i + 1]
    bakery[key] = int(value)

print(bakery)
