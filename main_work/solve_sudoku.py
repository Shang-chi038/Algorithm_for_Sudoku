from random import shuffle
from is_valid import is_valid

def solve_sudoku(board, stats=None):
    """
    Solve the sudoku board using backtracking.
    Returns True if solved, False if no solution exists.
    """

    # Create the stats dictionary
    if stats is None:
        stats = {'attempts': 0, 'backtracks': 0}
    
    # Scan the board to find the next empty cell (value 0)
    for row in range(9):
        for col in range(9):

            # If we find an empty cell
            if board[row][col] == 0:

                # Try values 1-9 in the empty cell
                values = [i for i in range(1, 10)]
                shuffle(values) # shuffled it for when I want to create different complete boards from an empty one using this function

                for val in values:
                    stats['attempts'] += 1  # Counts every attempt

                    # Only place `val` if that move is valid
                    if is_valid(board, row, col, val):
                        board[row][col] = val

                        # Recursively attempt to solve the rest of the board
                        if solve_sudoku(board):
                            return True  # If the rest of the board has been solved, return True
                            
                        # If recursion failed, move will not lead to a solution, then backtrack
                        stats['backtracks'] += 1  # Counts backtrack
                        board[row][col] = 0

                # If no value from 1–9 works in this cell, return False, same as 'else: return False', then bactrack
                return False

    # If we finished scanning without finding any empty cell, return True
    return True

'There will be a time when we wouold backtrack to the first move and try multiple things, and try multiple values in the first empty cell we saw, and nothing will work, the the board is unlsolvable'
