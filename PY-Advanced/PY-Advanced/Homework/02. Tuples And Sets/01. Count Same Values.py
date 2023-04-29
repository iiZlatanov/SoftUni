data = list(map(float, input().split()))
occurrences = {}

for element in data:
    if element not in occurrences:
        occurrences[element] = 1
    else:
        occurrences[element] += 1

for key, value in occurrences.items():
    print(f"{key:.1f} - {value} times")
