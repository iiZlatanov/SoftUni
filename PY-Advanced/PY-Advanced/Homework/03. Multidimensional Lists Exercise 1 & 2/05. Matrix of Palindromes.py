rows, cols = [int(x) for x in input().split(" ")]
matrix = [[] for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        if j == 0:
            char = chr(97 + i) * 3
        else:
            char = chr(97 + i) + chr(97 + i + j) + chr(97 + i)
        matrix[i].append(char)

for el in matrix:
    print(' '.join(el))
