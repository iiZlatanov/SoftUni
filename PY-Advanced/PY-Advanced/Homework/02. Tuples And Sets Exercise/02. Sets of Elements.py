two_numbers = tuple(map(int, input().split()))
tuple_one = tuple(int(input()) for x in range(two_numbers[0]))
tuple_two = tuple(int(input()) for y in range(two_numbers[1]))
result = []

for el in tuple_one:
    if el in tuple_two:
        result.append(el)

print("\n".join(set(map(str, result))))
