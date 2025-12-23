from display_board_r import display_board
from generate_complete_stats_r import generate_complete_board
from create_puzzle_r import create_puzzle
from solve_sudoku_stats_r import solve_sudoku

# # Generate a complete board
# complete = generate_complete_board()
# print("Complete board:")
# display_board(complete)

# # Create puzzles of different difficulties
# easy_puzzle = create_puzzle(complete, num_clues=45)
# medium_puzzle = create_puzzle(complete, num_clues=35)
# hard_puzzle = create_puzzle(complete, num_clues=25)

# print("\nEasy puzzle (45 clues):")
# display_board(easy_puzzle)

# print("\nMedium puzzle (35 clues):")
# display_board(medium_puzzle)

# print("\nHard puzzle (25 clues):")
# display_board(hard_puzzle)

# # Verify they can be solved
# stats = {'attempts': 0, 'backtracks': 0}
# if solve_sudoku(hard_puzzle, stats):
#     print(f"\nHard puzzle solved! Attempts: {stats['attempts']}, Backtracks: {stats['backtracks']}")


#######################################################################################
# board1 = generate_complete_board()
# board2 = generate_complete_board()
# board3 = generate_complete_board()

# print("Board 1 == Board 2?", board1 == board2)  # Should be False
# print("Board 2 == Board 3?", board2 == board3)  # Should be False


#######################################################################################
# from generate_complete_board import generate_complete_board
# from create_puzzle import create_puzzle
# from solve_sudoku_stats_r import solve_sudoku
# from display_board_r import display_board

# Step 1: Generate a complete board
print("Generating complete board...")
complete = generate_complete_board()
print("Complete board:")
display_board(complete)

# Step 2: Create puzzles of different difficulties
print("\n" + "="*50)
print("Creating Easy Puzzle (45 clues)...")
easy = create_puzzle(complete, num_clues=45)
display_board(easy)

print("\n" + "="*50)
print("Creating Medium Puzzle (30 clues)...")
medium = create_puzzle(complete, num_clues=30)
display_board(medium)

print("\n" + "="*50)
print("Creating Hard Puzzle (25 clues)...")
hard = create_puzzle(complete, num_clues=25)
display_board(hard)

# Step 3: Solve the hard puzzle and measure performance
print("\n" + "="*50)
print("Solving Hard Puzzle...")
stats = {'attempts': 0, 'backtracks': 0}
if solve_sudoku(hard, stats):
    print("\n✓ SOLVED!")
    display_board(hard)
    print(f"\nPerformance:")
    print(f"  Attempts: {stats['attempts']:,}")
    print(f"  Backtracks: {stats['backtracks']:,}")
    print(f"  Backtrack %: {stats['backtracks']/stats['attempts']*100:.2f}%")
else:
    print("✗ No solution found")
