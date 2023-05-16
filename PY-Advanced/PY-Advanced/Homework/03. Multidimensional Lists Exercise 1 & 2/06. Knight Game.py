ROWS_AND_COLS = int(input())
board = [list(input()) for _ in range(ROWS_AND_COLS)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
)
removed_knights = 0

while True:
    knight_pos_with_most_attacks = []
    max_attacks = 0

    for x in range(ROWS_AND_COLS):
        for y in range(ROWS_AND_COLS):
            attacks = 0

            if board[x][y] == "K":
                for el in positions:
                    if 0 <= x+el[0] < ROWS_AND_COLS and 0 <= y+el[1] < ROWS_AND_COLS:
                        if board[x+el[0]][y+el[1]] == "K":
                            attacks += 1

            if attacks > max_attacks:
                max_attacks = attacks
                knight_pos_with_most_attacks = (x, y)

    if knight_pos_with_most_attacks:
        i, j = knight_pos_with_most_attacks
        removed_knights += 1
        board[i][j] = "O"
    else:
        break

print(removed_knights)
