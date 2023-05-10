rows, cols = [int(x) for x in input().split(" ")]
matrix = [input().split(" ") for _ in range(rows)]
check_2x2_matrix = []
result = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            result += 1

print(result)
