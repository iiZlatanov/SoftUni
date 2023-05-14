rows, columns = list(map(int, input().split()))
matrix = []

for _ in range(rows):
    matrix.append(input().split())

command = input().split()

while command[0] != "END":
    if command[0] != "swap" or len(command) != 5 or int(command[1]) > (rows - 1) or int(command[2]) > (columns - 1) \
            or int(command[3]) > (rows - 1) or int(command[4]) > (columns - 1):
        print("Invalid input!")
    else:
        a = matrix[int(command[1])][int(command[2])]
        b = matrix[int(command[3])][int(command[4])]
        matrix[int(command[1])][int(command[2])] = b
        matrix[int(command[3])][int(command[4])] = a
        for each_list in matrix:
            for element in each_list:
                print(element, end=" ")
            print()
    command = input().split()
