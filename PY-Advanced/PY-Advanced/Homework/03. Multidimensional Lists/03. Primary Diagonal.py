rows_and_columns = int(input())
matrix = []
index = 0
primary_diagonal_sum = 0

for i in range(rows_and_columns):
    matrix.append(list(map(int, input().split())))

for k in range(rows_and_columns):
    primary_diagonal_sum += matrix[k][index]
    index += 1

print(primary_diagonal_sum)
