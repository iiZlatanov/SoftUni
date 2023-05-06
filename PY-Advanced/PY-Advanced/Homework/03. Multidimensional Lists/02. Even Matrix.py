# rows = int(input())
# matrix = []
#
# for row in range(rows):
#     data = [int(x) for x in input().split(", ")]
#     matrix.append([])
#     for el in data:
#         if el % 2 == 0:
#             matrix[row].append(el)
#
# print(matrix)

rows = int(input())
matrix = []
for _ in range(rows):
    current_row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(current_row)
print(matrix)
