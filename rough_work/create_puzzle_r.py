def create_puzzle(complete_board, num_clues=30):
    """
    Create a puzzle by removing numbers from a complete board.
    
    Args:
        complete_board: A fully filled valid Sudoku board
        num_clues: How many numbers to KEEP (rest will be removed)
    
    Returns:
        A puzzle board with some cells set to 0
    """
    import copy
    # Make a copy so we don't modify the original
    puzzle = copy.deepcopy(complete_board)  # Make a copy
    # puzzle = complete_board[:]

    removed = 81 - num_clues

    from random import randint as rint
    while removed > 0:
        row = rint(0,8)
        col = rint(0,8)

        # to skip alreasy empty cells
        if puzzle[row][col] == 0: continue

        puzzle[row][col] = 0
        removed -= 1

    return puzzle
