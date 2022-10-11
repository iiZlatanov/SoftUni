n = int(input())
uniques_collection = []

for name in range(n):
    data = input()
    if data not in uniques_collection:
        uniques_collection.append(data)

print("\n".join(uniques_collection))
