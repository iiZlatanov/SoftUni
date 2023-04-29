start = int(input())
end = int(input())
DIVISIBLES = [2, 3, 4, 5, 6, 7, 8, 9, 10]
result_list = []

for number in range(start, end + 1):
    for x in DIVISIBLES:
        if number % x == 0:
            result_list.append(number)
            break

print(result_list)
