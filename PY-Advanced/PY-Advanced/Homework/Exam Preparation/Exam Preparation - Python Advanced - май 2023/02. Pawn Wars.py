board = [input().split() for _ in range(8)]

for i in range(8):
    for j in range(8):
        if board[i][j] == "b":
            black_coords = [i, j]
        elif board[i][j] == "w":
            white_coords = [i, j]

white_letter_pos = chr(97 + white_coords[1])
black_letter_pos = chr(97 + black_coords[1])

if abs(black_coords[1] - white_coords[1]) > 1:
    upside_down_board = []
    for el in reversed(board):
        upside_down_board.append(el)

    for i in range(8):
        for j in range(8):
            if upside_down_board[i][j] == "b":
                black_coords_of_upside_down = [i, j]

    if white_coords[0] <= black_coords_of_upside_down[0]:
        print(f"Game over! White pawn is promoted to a queen at {white_letter_pos}8.")
    else:
        print(f"Game over! Black pawn is promoted to a queen at {black_letter_pos}1.")
else:
    index = 0
    while True:
        if white_coords[0] - black_coords[0] == 1:
            if index % 2 == 0:
                print(f"Game over! White win, capture on {black_letter_pos}{8 - black_coords[0]}.")
                break
            else:
                print(f"Game over! Black win, capture on {white_letter_pos}{8 - white_coords[0]}.")
                break
        else:
            if index % 2 == 0:
                white_coords[0] -= 1
            else:
                black_coords[0] += 1
        index += 1
