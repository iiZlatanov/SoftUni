rows, columns = list(map(int, input().split(", ")))
matrix = []
total = 0

for i in range(rows):
    matrix.append(list(map(int, input().split())))

for k in range(columns):
    sum_of_each_column = 0
    for j in range(rows):
        sum_of_each_column += matrix[j][k]
    print(sum_of_each_column)
