rows_and_cols = int(input())
matrix = []


def sum_of_primary_diagonal_of_square_matrix(matrix_data, matrix_dimensions):
    total = 0

    for i in range(matrix_dimensions):
        for j in range(matrix_dimensions):
            if i == j:   #since this is a square matrix, every time we have the same 2 indexes(same numbers) we will be accessing the diagonal of the matrix
                total += int(matrix_data[i][j])

    return total


def sum_of_secondary_diagonal_of_square_matrix(matrix_data, matrix_dimensions):
    mirrored_matrix = []
    index = 0
    for el in matrix_data:
        mirrored_matrix.append([])
        for _ in range(matrix_dimensions):
            mirrored_matrix[index].append(el.pop())
        index += 1

    return sum_of_primary_diagonal_of_square_matrix(mirrored_matrix, matrix_dimensions)


def absolute_difference_of_diagonals_of_square_matrix(matrix_data, matrix_dimensions):
    a = sum_of_primary_diagonal_of_square_matrix(matrix_data, matrix_dimensions)
    b = sum_of_secondary_diagonal_of_square_matrix(matrix_data, matrix_dimensions)

    return abs(a - b)


for _ in range(rows_and_cols):
    matrix.append(input().split(" "))

print(absolute_difference_of_diagonals_of_square_matrix(matrix, rows_and_cols))
