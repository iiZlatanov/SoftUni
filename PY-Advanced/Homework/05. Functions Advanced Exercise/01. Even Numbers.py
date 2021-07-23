data = [int(el) for el in input().split()]

result = filter(lambda x: x % 2 == 0, data)

print(list(result))
