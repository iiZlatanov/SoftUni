from collections import deque
from copy import copy

rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()]for _ in range(rows)]

def is_the_command_valid(*args):
    validity = False

    if len(args[0]) == 5:
        if args[0][0] == "swap":
            if int(args[0][1]) >= 0 and int(args[0][2]) >= 0:
                if matrix[int(args[0][1])][int(args[0][2])]:
                    if int(args[0][3]) >= 0 and int(args[0][4]) >= 0:
                        if matrix[int(args[0][3])][int(args[0][4])]:
                            validity = True

    return validity


command = input()
while command != "END":
    if is_the_command_valid(command.split()):
        command = command.split()
        coord_a = int(command[1])
        coord_b = int(command[2])
        coord_c = int(command[3])
        coord_d = int(command[4])
        matrix_copy = copy(matrix)
        matrix[coord_a][coord_b] = matrix_copy[coord_c][coord_d]
        matrix[coord_c][coord_d] = matrix_copy[coord_a][coord_b]
        print(matrix)
    else:
        print("Invalid input!")

    command = input()