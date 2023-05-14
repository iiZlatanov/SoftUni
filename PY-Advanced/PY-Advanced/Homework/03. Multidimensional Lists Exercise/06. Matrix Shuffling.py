rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for x in range(rows)]

while True:
    command, *info = [int(x) if x.isdigit() else str(x) for x in input().split()]
    if command == "END":
        break
    if command == "swap":
        if len(info) == 4:
            coord_a, coord_b, coord_c, coord_d = [int(x) for x in info]

            if command == "swap" and coord_a < rows and coord_c < rows and coord_b < cols and coord_d < cols:
                matrix[coord_a][coord_b], matrix[coord_c][coord_d] = matrix[coord_c][coord_d], matrix[coord_a][coord_b]

                for el in matrix:
                    print(" ".join(el))
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
