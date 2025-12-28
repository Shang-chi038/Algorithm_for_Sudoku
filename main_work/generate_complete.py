from solve_sudoku import solve_sudoku

def generate_complete_board():
    """Generate a random complete valid Sudoku board."""
    board = [[0]*9 for _ in range(9)]
    
    solve_sudoku(board)

    return board
