rows, columns = list(map(int, input().split()))
matrix = []
word = input()
snake = []
index = 0
for el in word:
    snake.append(el)
for n in range(rows):
    matrix.append([])

for i in range(rows):
    if i % 2 == 0:
        for _ in range(columns):
            matrix[i].append(snake[index])
            index += 1
            if index == len(snake):
                index = 0
    else:
        for _ in range(columns):
            matrix[i].insert(0, snake[index])
            index += 1
            if index == len(snake):
                index = 0

for each_list in matrix:
    for element in each_list:
        print(element, end="")
    print()
