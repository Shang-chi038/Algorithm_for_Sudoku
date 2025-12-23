from is_valid import is_valid

def solve_sudoku(board):
    """
    Solve the sudoku board using backtracking.
    Returns True if solved, False if no solution exists.
    """
    # Scan the board to find the next empty cell (value 0)
    for row in range(9):
        for col in range(9):

            # If we find an empty cell
            if board[row][col] == 0:

                # Try values 1-9 in the empty cell
                for val in range(1, 10):
                    # Only place `val` if that move is valid
                    if is_valid(board, row, col, val):
                        board[row][col] = val

                        # Recursively attempt to solve the rest of the board
                        if solve_sudoku(board):
                            return True  # If the rest of the board has been solved, return True
                            
                        # If move will not lead to a solution, backtrack
                        board[row][col] = 0

                # If no value from 1–9 works in this cell, return False, same as 'else: return False', then bactrack
                return False

    # If we finished scanning without finding any empty cell, return True
    return True

'There will be a time when we wouold backtrack to the first move and try multiple things, and try multiple values in the first empty cell we saw, and nothing will work, the the board is unlsolvable'
