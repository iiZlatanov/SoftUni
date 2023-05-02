data = input()
counter = {}

for ch in data:
    if ch not in counter:
        counter[ch] = 0

    counter[ch] += 1

for key, value in sorted(counter.items()):
    print(f"{key}: {value} time/s")
