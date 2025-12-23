# # Testing the is_valid function
# from is_valid import is_valid


# # Test 1: Empty board - all values should be valid
# print("Test 1: Empty board - all values should be valid")
# board = [[0]*9 for _ in range(9)]
# print(is_valid(board, 0, 0, 1))  # Should be True
# print(is_valid(board, 0, 0, 9))  # Should be True

# # Test 2: Value in same row
# print("\nTest 2: Value in same row")
# board = [[0]*9 for _ in range(9)]
# board[0][5] = 5
# print(is_valid(board, 0, 0, 5))  # Should be False (5 in row 0)
# print(is_valid(board, 0, 0, 3))  # Should be True

# # Test 3: Value in same column
# print("\nTest 3: Value in same column")
# board = [[0]*9 for _ in range(9)]
# board[5][0] = 7
# print(is_valid(board, 0, 0, 7))  # Should be False (7 in column 0)
# print(is_valid(board, 0, 0, 2))  # Should be True

# # Test 4: Value in same box
# print("\nTest 4: Value in same box")
# board = [[0]*9 for _ in range(9)]
# board[1][1] = 4
# print(is_valid(board, 0, 0, 4))  # Should be False (4 in box 0,0)
# print(is_valid(board, 0, 0, 6))  # Should be True


from solve_sudoku import solve_sudoku
from display_board import display_board

# Easy test case - almost complete
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Usage:
stats = {'attempts': 0, 'backtracks': 0}
if solve_sudoku(board, stats):
    print(f"Solved!")
    print(f"Total attempts: {stats['attempts']}")
    print(f"Total backtracks: {stats['backtracks']}")
    display_board(board)
else:
    print("No solution exists")
