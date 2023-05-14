rows_and_columns = int(input())
matrix = []
primary_diagonal = 0
secondary_diagonal = 0
index = rows_and_columns - 1

for _ in range(rows_and_columns): #Creating the matrix
    matrix.append(list(map(int, input().split())))

for i in range(rows_and_columns):
    primary_diagonal += matrix[i][i]

for k in range(rows_and_columns):
    secondary_diagonal += matrix[k][index]
    index -= 1

print(abs(primary_diagonal - secondary_diagonal))
