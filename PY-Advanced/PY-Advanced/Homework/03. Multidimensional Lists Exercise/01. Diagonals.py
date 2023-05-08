rows_and_columns = int(input())
matrix = []
mirrored_matrix = []
primary_diagonal = []
secondary_diagonal = []
index = 0

for _ in range(rows_and_columns):
    matrix.append(input().split(", "))

for i in range(rows_and_columns):
    for j in range(rows_and_columns):
        element = int(matrix[i][j])
        if i == j:
            primary_diagonal.append(element)

for el in matrix:
    mirrored_row = []
    for _ in range(rows_and_columns):
        mirrored_row.append(el.pop())
    secondary_diagonal.append(int(mirrored_row[index]))
    index += 1

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}"
      f"\nSecondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
