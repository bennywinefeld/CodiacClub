Yasha = [' ']*9
Yasha[3] = "X"
Yasha[4] = "Y"

Papa = [' ']*9
Papa[2] = "Z"

def printBoard(board):
    print("Inside function printBoard variable board =")
    print(board)
    print("+---+---+---+")
    print("| {} | {} | {} |".format(board[0],board[1],board[2]))
    print("+---+---+---+")
    print("| {} | {} | {} |".format(board[3],board[4],board[5]))
    print("+---+---+---+")
    print("| {} | {} | {} |".format(board[6],board[7],board[8]))
    print("+---+---+---+")


printBoard(Yasha)
printBoard(Papa)