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

