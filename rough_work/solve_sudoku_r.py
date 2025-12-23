# from is_valid_r import is_valid

# def solve_sudoku(board, stats=None):
#     """
#     Solve the sudoku board using backtracking.
#     """
#     if stats is None:
#         stats = {'attempts': 0, 'backtracks': 0}
    
#     for row in range(9):
#         for col in range(9):
#             if board[row][col] == 0:
#                 for val in range(1, 10):
#                     stats['attempts'] += 1  # Count each attempt
                    
#                     if is_valid(board, row, col, val):
#                         board[row][col] = val
                        
#                         if solve_sudoku(board, stats):
#                             return True
                        
#                         stats['backtracks'] += 1  # Count backtrack
#                         board[row][col] = 0
                
#                 return False
    
#     return True
from random import shuffle as shf
from is_valid_r import is_valid
def solve_sudoku(board):
    """
    Solve the sudoku board using backtracking.
    Modifies the board in-place.
    Returns True if solved, False if no solution exists.
    """
    
    # Step 1: Find the next empty cell (value == 0)
    # Hint: Use nested loops to scan the board
    # If you find an empty cell, store its position
    # If no empty cells found, the board is complete!
    # TODO: Your code here to find empty cell
    # If no empty cell found, return True (solved!)

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                empty_cell = [row, col] 
        
                # Step 2: Try values 1-9 in this empty cell
                value = [i for i in range(1, 10)]
                shf(value)

                for val in value:   
                # Step 3: Check if this value is valid
                # TODO: Use your is_valid() function
                    if is_valid(board, empty_cell[0], empty_cell[1], val):
                    # Step 4: If valid, place the value
                    # TODO: board[row][col] = value
                        board[row][col] = val
                    else: # This value violates constraints, skip it and try the next value in the loop
                        continue
                    # Step 5: Recursively solve the rest of the board
                    # TODO: if solve_sudoku(board):
                    #           return True  # Success!
                    if solve_sudoku(board): return True
                        # Step 6: If recursion failed, backtrack
                        # TODO: board[row][col] = 0  # Undo the placement
                    else:
                        board[row][col] = 0
                        continue
                # Step 7: If no value worked, return False
                # TODO: return False
                else: return False
            
    # if no epmpty cells were found
    else:
        return True
        