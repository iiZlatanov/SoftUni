rows, cols = [int(x) for x in input().split(" ")]
matrix = [[int(x) for x in input().split(" ")] for _ in range(rows)]
result = float("-inf")
result_submatrix = []

for x in range(rows - 2):
    for y in range(cols - 2):
        first_row = matrix[x][y:y + 3]
        second_row = matrix[x + 1][y:y + 3]
        third_row = matrix[x + 2][y:y + 3]
        matrix_3x3_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if matrix_3x3_sum > result:
            result = matrix_3x3_sum
            result_submatrix = [first_row, second_row, third_row]

print(f"Sum = {result}")
for row in result_submatrix:
    print(*row)
