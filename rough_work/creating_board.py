# A function to randomly generate a simple sudoku table
from random import randint, randrange
from board_me import display_board


no_of_fillled_spaces = 27
no_of_empty_spaces = 81 - no_of_fillled_spaces

board = [[0 for _ in range(9)] for _ in range(9)]
positions = []

# for i in range(27):
#     row = randrange(0,9)
#     col = randrange(0,9)
#     value = randrange(1,10)
#     board[row][col] = value
# print(board)
# 22 on the table
# first row - [0]
# board[0][1] = 6
# board[0][2] = 4
# board[0][5] = 2

# # second row - [1]
# board[1][4] = 4
# board[1][6] = 5
# board[1][7] = 9

# # third row - [2]
# board[2][0] = 2
# board[2][2] = 7
# board[2][3] = 6
# board[2][4] = 3
# board[2][6] = 8
# board[2][8] = 1

# # fourth row - [3]
# board[3][0] = 1
# board[3][5] = 7
# board[3][7] = 4

# # fifth row - [4]

# # sixth row - [5]
# board[5][3] = 9
# board[5][7] = 2

# # seventh row - [8]
# board[6][3] = 3
# board[6][8] = 9

# # eight row - [8]
# board[7][1] = 5
# board[7][2] = 8
# board[7][4] = 2
# board[7][6] = 6
# board[7][7] = 3

# # ninth row - [1]
# board[8][2] = 9
# board[8][3] = 1
# board[8][5] = 5



counter = 0
while counter < 81:
    row = randrange(9)
    col = randrange(9)
    value = randrange(1, 10)

    # skips a filled cell
    if board[row][col] != 0:
        continue

    # skip immediately if the row already contains this value
    if value in board[row]:
        continue

    # scan the column; break if a duplicate appears
    for i in range(9):
        if board[i][col] == value:
            break
    else:
        # column is clean; now locate the 3×3 block that (row, col) belongs to
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        # walk the 3×3 block; break out if the value is already present
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if board[r][c] == value:
                    break
            else:
                continue  # inner loop didn’t break, keep scanning block
            break
        else:
            # row, column, and block all clear — place the value
            board[row][col] = value
            # display_board(board)
            counter += 1

display_board(board)
