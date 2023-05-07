rows_of_matrix, columns_of_matrix = [int(x) for x in input().split(", ")]
matrix = []
current_sum = 0
max_sum = 0
current_submatrix = []
result_submatrix = []
index = 0

for _ in range(rows_of_matrix):
    matrix.append(input().split(", "))


for x in range(rows_of_matrix - 1):
    for i in range(columns_of_matrix - 1):
        current_sum += int(matrix[x][i])
        current_sum += int(matrix[x + 1][i])
        current_sum += int(matrix[x][i + 1])
        current_sum += int(matrix[x + 1][i + 1])
        current_submatrix.append(matrix[x][i])
        current_submatrix.append(matrix[x + 1][i])
        current_submatrix.append(matrix[x][i + 1])
        current_submatrix.append(matrix[x + 1][i + 1])
        if current_sum > max_sum:
            max_sum = current_sum
            result_submatrix = current_submatrix
        current_submatrix = []
        current_sum = 0

result_manipulation = [
    [result_submatrix[0], result_submatrix[2]],
    [result_submatrix[1], result_submatrix[3]]
]

for sublist in result_manipulation:
    print(" ".join(sublist))
print(max_sum)
