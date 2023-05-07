# # First way
# rows_of_matrix = int(input())
# matrix = []
# result = 0
#
# for _ in range(rows_of_matrix):
#     matrix.append(input().split(" "))
#
# for i in range(rows_of_matrix):
#     for j in range(rows_of_matrix):
#         if j == i:
#             result += int(matrix[i][j])
#
# print(result)

# # Second way
rows_of_matrix = int(input())
matrix = []
result = 0

for _ in range(rows_of_matrix):
    matrix.append(input().split(" "))

for x in range(rows_of_matrix):
    result += int(matrix[x][x])

print(result)
