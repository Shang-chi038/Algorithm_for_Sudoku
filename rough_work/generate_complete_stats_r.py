from is_valid_r import is_valid
from solve_sudoku_stats_r import solve_sudoku
from display_board_r import display_board

def generate_complete_board():
    """Generate a random complete valid Sudoku board."""
    board = [[0]*9 for _ in range(9)]
    # print("\nEmpty board")
    # display_board(board)
    solve_sudoku(board)

    # print("\n\nComplete board")
    return board

# def main():
#     b1 = generate_complete_board()
#     b2 = generate_complete_board()
#     b3 = generate_complete_board()
#     b4 = generate_complete_board()
#     b5 = generate_complete_board()
#     print(b1 == b2)
#     print(b1 == b3)
#     print(b1 == b4)
#     print(b1 == b5)
#     print(b2 == b3)
#     print(b2 == b4)
#     print(b2 == b5)
#     print(b3 == b4)
#     print(b3 == b5)
#     print(b4 == b5)
#     display_board(b1)
#     display_board(b2)
#     # print(b)

# main()
