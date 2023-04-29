data = map(float, input().split(" "))
results = {}

for el in data:
    if el not in results:
        results[el] = 0
    results[el] += 1

for (value, count) in results.items():
    print(f"{value} - {count} times")
