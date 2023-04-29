text = input()
collection = {}

for element in text:
    if element not in collection:
        collection[element] = 1
    else:
        collection[element] += 1

sorted_collection = sorted(collection.items(), key=lambda x: x[0])
for el in sorted_collection:
    print(f"{el[0]}: {el[1]} time/s")
