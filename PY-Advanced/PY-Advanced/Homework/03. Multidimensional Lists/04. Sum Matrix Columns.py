rows_of_matrix, columns_of_matrix = [int(x) for x in input().split(", ")]
matrix = []

for i in range(rows_of_matrix):
    data = [int(x) for x in input().split(" ")]
    matrix.append(data)

for i in range(columns_of_matrix):
    result = 0
    for j in range(rows_of_matrix):
        result += matrix[j][i]
    print(result)
