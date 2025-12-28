from display_board_r import display_board
board = [[0 for i in range(9)]for i in range(9)]
board[2][3] = 5
#  A function to accept user's move
move = int(input("Enter the number you want to play: "))
cell = input("Enter the position you want to play in (e.g. 2,3 meaning row 2, column 3): ")

cell = cell.split(',')

for i in range(2):
    cell[i] = int(cell[i])-1

board[cell[0]][cell[1]] = move

# return board

display_board(board)


# print(position)
# print(type(position))
