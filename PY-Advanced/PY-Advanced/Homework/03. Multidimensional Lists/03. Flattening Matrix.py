rows_of_matrix = int(input())
flattened_matrix = []

# with comprehension
# for _ in range(rows_of_matrix):
#     data = [flattened_matrix.append(int(x)) for x in input().split(", ")]

# print(flattened_matrix)

for _ in range(rows_of_matrix):
    data = [int(x) for x in input().split(", ")]
    for el in data:
        flattened_matrix.append(el)

print(flattened_matrix)
