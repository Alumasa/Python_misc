#BATTLESHIP GAME
#import random module
from random import randint

board = []

#arrange Os in the board 5x5
for x in range(0, 5):
  board.append(["O"] * 5)

#join the Os by removing ""
#take note of python3 method of joining strings
def print_board(board):
    for row in board:
        s = " "
        print(s.join(row))

print_board(board)

#functions to return random indexes in row and column, where we'll hide our ship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#call the above functions to know where the ship is randomly hidden
ship_row = random_row(board)
ship_col = random_col(board)
#print the location of the ship while debugging, comment out while playing
#print ship_row
# print ship_col

# Everything from here on should be in your for loop to count the turns on each iteration
# conditions are for winning, missing, out of range and repeating a guess.
for turn in range(4):
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(5) or \
            guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print("Game Over")
    print_board(board)
#It works!!
#Challenge enhancements:
# make the game a two-player
#make the game bigger or smaller than 5x5
#I'll come back to tweek it after I learn more.
