data = [int(x) for x in input().split()]
result = []

while len(data) > 0:
    result.append(str(data.pop()))

print(" ".join(result))
