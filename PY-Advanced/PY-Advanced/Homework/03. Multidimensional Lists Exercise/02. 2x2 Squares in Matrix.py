rows, columns = list(map(int, input().split()))
matrix = []
check_list = []
result_counter = 0

for _ in range(rows):
    matrix.append(input().split())

rightmost_index_to_go = columns - 1
bottommost_index_to_go = rows - 1
index = rightmost_index_to_go


for i in range(bottommost_index_to_go):
    for k in range(rightmost_index_to_go):
        check_list = []
        check_list.append(matrix[i][k])
        check_list.append(matrix[i][k + 1])
        check_list.append(matrix[i + 1][k])
        check_list.append(matrix[i + 1][k + 1])
        if len(set(check_list)) == 1:
            result_counter += 1

print(result_counter)
