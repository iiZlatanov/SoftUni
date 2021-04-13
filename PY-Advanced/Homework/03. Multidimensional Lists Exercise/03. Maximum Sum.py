rows, columns = list(map(int, input().split()))
matrix = []
rightmost_possible_index = columns - 2
bottommost_possible_index = rows - 2
current_sum = 0
max_sum = 0
result_matrix = []
current_matrix = [
    [],
    [],
    [],
]

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

for i in range(bottommost_possible_index):
    for k in range(rightmost_possible_index):
        current_matrix = [
            [],
            [],
            [],
        ]
        current_matrix[0].append(matrix[i][k])
        current_matrix[0].append(matrix[i][k + 1])
        current_matrix[0].append(matrix[i][k + 2])
        current_matrix[1].append(matrix[i + 1][k])
        current_matrix[1].append(matrix[i + 1][k + 1])
        current_matrix[1].append(matrix[i + 1][k + 2])
        current_matrix[2].append(matrix[i + 2][k])
        current_matrix[2].append(matrix[i + 2][k + 1])
        current_matrix[2].append(matrix[i + 2][k + 2])
        current_sum = 0
        for each_list in current_matrix:
            for element in each_list:
                current_sum += element
        if current_sum > max_sum:
            max_sum = current_sum
            result_matrix = current_matrix

print(f"Sum = {max_sum}")
for lists in result_matrix:
    for each_element in lists:
        print(f"{each_element}", end=" ")
    print()
