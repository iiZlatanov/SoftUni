square_matrix_rows_and_cols = int(input())
matrix = []

for _ in range(square_matrix_rows_and_cols):
    matrix.append(input())

symbol = input()
flag = True

for i in range(square_matrix_rows_and_cols):
    for j in range(square_matrix_rows_and_cols):
        if matrix[i][j] == symbol:
            print(f"({i}, {j})")
            flag = False
            break

if flag is True:
    print(f"{symbol} does not occur in the matrix")
