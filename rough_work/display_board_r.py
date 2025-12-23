# # An function to print a sudoku board
# board = [] # a variable to store the contents on my table

# # a loop to fill my board with values
# for i in range(1, 10): # a loop to fill the board column-wise
#     temp = [] # a variable used to temporarily house the value in each column

#     for i in range(1, 10): # a loop to fill the board row-wise
#         # print(i, end=", ") # used to print the values in a row
#         temp.append(i) # used to add the values of a row to temp
    
#     board.append(temp) # used to add each row to the table
#     # print("\b\b \b\b") # used to delete the ', ' at the end of every row that is printed, and the ' ' is to activate the first 2 '\b'

# # print(board) # used to see what the board now looks like

# print("\n") # to jump one line with 
# board = [[0 for i in range(9)]for i in range(9)] # a variable to store the contents on my table a filled with 9 lists of zeroes using list comprehension

# board[2][3] = 5
# for i in range(1,10):
#     if i%3!=0: print("_---", end="")
#     else: print("__---", end="")
# # counter = 0 # a variable used to indicate your current position in rows on the board
# for row in range(9):
#     print("\n|", end=" ")
#     for col in range(9):
#         # if col==0: # if the part of that board does not containg a value yet, it is still zero
#         if board[row][col]==0: # if the part of that board does not containg a value yet, it is still zero
#             print(" ", end=" | ") # print a space the size of a digit
#         else:
#             print(board[row][col], end=" | ") # print what is at that position in the board
        
#         if (col+1)%3 ==0:
#             print("\b| ", end="") # I printed a second '|' after every 3 cells, and added 'end=""' to prevent it from creating a newline after printing
#         # print(col, end=" | ")
#         # counter += 1 # increasing the counter by 1 to indicate that the loop is moving to the next column - it is redudndant because it is already using two lines, why not just use 'range(9)' to replace board in the outer loop and row in the inner loop.
    
#     # print() # to add a newline before continuing the printing of the next row
#     if (row+1)%3==0: # if any row's number, not index can be divided by 3
#         print(end="\n ")
#         for i in range(9):
#             if (i+1)%3==0 and i!=0: print("---  ", end="")
#             else: print("--- ", end="")
            # print("\n", "--- "*9, end="") # print a demacation, dividing the board into 9 small squares, 'end=""' to prevent a newline creation after print, so that the '\n|' continues on the next line without an additional newline
# print("----"*9, end="-\n")


# TESTING IDEAS
# print(board[2[3]]) # If it is possible to indent a list using a list of lists - it did not work

# board.append(0)
# print(board)



def display_board(board):
    print("_", end="")
    for i in range(1,10):
        if (i)%3==0: print("---__", end="")
        else: print("---_", end="")
    
    for row in range(9):
        print("\n|", end=" ")
        for col in range(9):
            
            if board[row][col]==0: # if the part of that board does not containg a value yet, it is still zero
                print(" ", end=" | ") # print a space the size of a digit
            else:
                print(board[row][col], end=" | ") # print what is at that position in the board
            
            if (col+1)%3 ==0:
                print("\b| ", end="") # I printed a second '|' after every 3 cells, and added 'end=""' to prevent it from creating a newline after printing
            
        if (row+1)%3==0: # if any row's number, not index can be divided by 3
            print(end="\n ")
            for i in range(9):
                if (i+1)%3==0 and i!=0: print("---  ", end="")
                else: print("--- ", end="")
                # print("\n", "--- "*9, end="") # print a demacation, dividing the board into 9 small squares, 'end=""' to prevent a newline creation after print, so that the '\n|' continues on the next line without an additional newline
    
