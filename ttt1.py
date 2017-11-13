# Board is represented by an array with indexes from 0 to 0
# each array element can contain values: ' ','X','O'
def drawBoard(board):
    print("+---+---+---+")
    for i in range(3):
        print("| {} | {} | {} |".format(board[3*i],board[3*i+1],board[3*i+2]))
        print("+---+---+---+")


# Insert X or O to board, for ex: makeMove(myBoard,'X',3)
def makeMove(board,X_or_O,position):
    if(board[position] != ' '):
        print("This cell is already taken, choose another")
        return False
    board[position] = X_or_O
    return True

# Check if current player won by the last move
# Variable b stands for board. Used one letter var name to make expressions look short 
def checkIfWon(b,X_or_O):
    w = X_or_O * 3    
    if ((b[0]+b[1]+b[2] == w) or (b[3]+b[4]+b[5] == w) or (b[6]+b[7]+b[8] == w) or (b[0]+b[3]+b[6] == w) or \
    (b[1]+b[4]+b[7] == w) or (b[2]+b[5]+b[8] == w) or (b[0]+b[4]+b[8] == w) or (b[2]+b[4]+b[6] == w)):
        return True    
    return False


# Initialize the game
#  Reset the board with all ' ', set gameOver flag to False, player 'X' starts first
myBoard = [' ']*9
gameOver = False
nowPlays = 'X' 
drawBoard(myBoard)

# Start the game and continue until someone wins or board is full
while (not gameOver):
    # Ask current player to make a move. Repeat asking if move is illegal
    position = int(input(nowPlays + " where do you want to go (1-9)? ")) - 1
    while (not makeMove(myBoard,nowPlays,position)):
        position = int(input(nowPlays + " where do you want to go (1-9)? ")) - 1
    
    # Draw the board to display all the cells filled so far
    drawBoard(myBoard)
    print(myBoard)

    # Check if the last move has won the game
    if (checkIfWon(myBoard,nowPlays)):
        print(nowPlays + " , you have won!")
        gameOver = True

    # Check if board is full. If yes, it's a tie!
    if (not ' ' in myBoard):
        print("It's a tie!")
        gameOver = True

    # Switch current player
    if (nowPlays == 'X'):
        nowPlays = 'O'
    else:
        nowPlays = 'X'
