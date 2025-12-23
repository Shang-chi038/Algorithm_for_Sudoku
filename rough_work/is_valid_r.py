# # A function to check if a move is valid
# def is_valid(board, row, col, value): 
#     # Check if value exists in the 3x3 box
#     found_in_box = False
#     start_row = (row // 3) * 3
#     start_col = (col // 3) * 3

#     for r in range(start_row, start_row + 3):
#         for c in range(start_col, start_col + 3):
#             if board[r][c] == value:
#                 found_in_box = True
#             break
#         if found_in_box:
#             break

#     # if not found_in_box:
#     #     board[row][col] = value
#     #     counter += 1



#     # if board[row][col] == value:
#     #     return False
    
#     # To check if there is a similar value in the row
#     found_in_row = False
#     for current_cell in board[row]:
#         if value == current_cell: 
#             found_in_row = True
#         # break
#             break

#     found_in_col = False
#     # to check if there is a similar value in the column
#     for current_row in range(9):
#         if value == board[col][current_row]:
#             found_in_col = True
#         # break
#             break
    

#     # returning my decision
#     # return (not(found_in_box and found_in_row and found_in_col))
#     return (not(found_in_box or found_in_row or found_in_col))
    
# A function to check if a move to be made while creating a board is valid
def is_valid(board, row, col, value): 
    """
    Check if placing 'value' at board[row][col] is valid.
    Returns True if valid, False otherwise.
    """

    # Check if value exists in the 3x3 box
    found_in_box = False
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == value:
                found_in_box = True
                break
        if found_in_box:
            break
    
    # To check if there is a similar value in the row
    found_in_row = False
    for current_cell in board[row]:
        if value == current_cell: 
            found_in_row = True
            break

    # to check if there is a similar value in the column
    found_in_col = False
    for current_row in range(9):
        if value == board[current_row][col]:
            found_in_col = True
            break
    

    # returning my decision
    return not (found_in_box or found_in_row or found_in_col)
    