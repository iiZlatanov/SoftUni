rows, columns = list(map(int, input().split(", ")))
matrix = []
total = 0

for i in range(rows):
    numbers_data = list(map(int, input().split(", ")))
    matrix.append([])
    for element in numbers_data:
        total += element
        matrix[-1].append(element)

print(total)
print(matrix)
