from collections import deque
rows, cols = [int(x) for x in input().split()]
word = deque()
matrix = []

for ch in input():
    word.append(ch)

while len(matrix) < rows:
    data = ""
    for x in range(cols):
        leftmost_char = word.popleft()
        word.append(leftmost_char)
        data += leftmost_char

    if len(matrix) == 0 or len(matrix) % 2 == 0:
        matrix.append(list(data))
    else:
        matrix.append(list(map(str, reversed(data))))

[print(''.join(row))for row in matrix]
