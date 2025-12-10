# A function to check if a move to be made while creating a board is valid
def is_valid(board, row, col, value): 
    """
    Check if placing 'value' at board[row][col] is valid.
    Returns True if valid, False otherwise.
    """

    # Check if value exists in the 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == value:
                return False
    
    # To check if there is a similar value in the row
    if value in board[row]:
        return False


    # to check if there is a similar value in the column
    for current_row in range(9):
        if value == board[current_row][col]:
            return False
    
    # if all checks pass, return True
    return True
