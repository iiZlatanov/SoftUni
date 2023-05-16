ROWS_AND_COLS = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(ROWS_AND_COLS)]
ERROR_MESSAGE = "Invalid coordinates"

def add_or_subtract(command, *args):
    if command == "Add":
        coordinate_x = int(args[0])
        coordinate_y = int(args[1])
        if 0 <= coordinate_x < ROWS_AND_COLS and 0 <= coordinate_y < ROWS_AND_COLS:
            matrix[coordinate_x][coordinate_y] += int(args[2])
        else:
            print(ERROR_MESSAGE)
    elif command == "Subtract":
        coordinate_x = int(args[0])
        coordinate_y = int(args[1])
        if 0 <= coordinate_x < ROWS_AND_COLS and 0 <= coordinate_y < ROWS_AND_COLS:
            matrix[coordinate_x][coordinate_y] -= int(args[2])
        else:
            print(ERROR_MESSAGE)
    else:
        print(ERROR_MESSAGE)


while True:
    data = input()
    if data == "END":
        for submatrix in matrix:
            print(" ".join(map(str, submatrix)))
        break
    else:
        data = data.split()
        if len(data) == 4:
            add_or_subtract(*data)
        else:
            print(ERROR_MESSAGE)
