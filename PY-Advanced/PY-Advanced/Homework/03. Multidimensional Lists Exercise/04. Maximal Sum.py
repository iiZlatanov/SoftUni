rows, cols = [int(x) for x in input().split(" ")]
matrix = []
result = 0
result_submatrix = []

for x in range(rows):
    data = input().split(" ")
    matrix.append(data)

for x in range(rows - 2):
    for y in range(cols - 2):
        submatrix = [
            [],
            [],
            []
        ]
        a = int(matrix[x][y])
        b = int(matrix[x][y + 1])
        c = int(matrix[x][y + 2])
        d = int(matrix[x + 1][y])
        e = int(matrix[x + 1][y + 1])
        f = int(matrix[x + 1][y + 2])
        g = int(matrix[x + 2][y])
        h = int(matrix[x + 2][y + 1])
        i = int(matrix[x + 2][y + 2])
        matrix_3x3_sum = a + b + c + d + e + f + g + h + i
        submatrix[0].append(a)
        submatrix[0].append(b)
        submatrix[0].append(c)
        submatrix[1].append(d)
        submatrix[1].append(e)
        submatrix[1].append(f)
        submatrix[2].append(g)
        submatrix[2].append(h)
        submatrix[2].append(i)
        if matrix_3x3_sum > result:
            result = matrix_3x3_sum
            result_submatrix = submatrix

print(f"Sum = {result}")
for row in result_submatrix:
    print(*row)
