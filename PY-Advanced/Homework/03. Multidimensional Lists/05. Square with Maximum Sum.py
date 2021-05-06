rows, columns = input().split(", ")
matrix = []
rightmost_index = int(columns) - 1
bottommost_index = int(rows) - 1
total = 0
current_matrix = [
    [],
    []
]

max_sum_matrix = [
    [],
    []
]

for _ in range(int(rows)):
    matrix.append(list(map(int, input().split(', '))))

for i in range(bottommost_index):
    for k in range(rightmost_index):
        current_matrix = [
            [],
            []
        ]
        current_matrix[0].append(matrix[i][k])
        current_matrix[0].append(matrix[i][k + 1])
        current_matrix[1].append(matrix[i + 1][k])
        current_matrix[1].append(matrix[i + 1][k + 1])
        if sum(current_matrix[0]) + sum(current_matrix[1]) > sum(max_sum_matrix[0]) + sum(max_sum_matrix[1]):
            max_sum_matrix = current_matrix

for mini_matrix in max_sum_matrix:
    for numbers in mini_matrix:
        total += numbers
    print(" ".join(list(map(str, mini_matrix))))
print(total)
