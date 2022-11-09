#Implementation of Two Player Tic-Tac-Toe game in Python.
#Created a dictionary of length 9, each key represents a block
#on the board and its value represents the move made by the player

''' We will make the board using dictionary
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initially it's values will be empty space and then after every move
    we will change the value according to player's choice of move. '''
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)
''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

#Create a function which we use everytime I want the board
#print the updated board in the game
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#THIS IS WHAT THE BOARD LOOKS LIKE
#  | |
# -+-+-
#  | |
# -+-+-
#  | |

#The main func. we are taking the input from the player
#and check if the input is a valid move or not.
#If the block the player chooses to move to a block we will
#fill that block otherwise we will ask the user to choose another block

def game():

    turn = 'X' #<-- Player1
    count = 0 #<-- Player2

    for i in range(10):
            printBoard(theBoard)
            print("It's your turn," + turn + ".Move to which place?")

            move = input()

            if theBoard[move] == ' ': #<-- Empty space
                theBoard[move] = turn #<-- Fill in space
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue

#Checking winning conditions, checking a total of 8 conditions and
#which player made the last move, we will declare that player as a winner
#and if no one wins, we declare 'tie'
# Now we will check if player X or O has won,for every move after 5 moves.
            if count >= 5:
                if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                   printBoard(theBoard)
                   print("\nGame Over.\n")
                   print(" **** " +turn + " won. ****")
                   break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                   printBoard(theBoard)
                   print("\nGame Over.\n")
                   print(" **** " +turn + " won. ****")
                   break
                elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                   printBoard(theBoard)
                   print("\nGame Over.\n")
                   print(" **** " +turn + " won. ****")
                   break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                   printBoard(theBoard)
                   print("\nGame Over.\n")
                   print(" **** " +turn + " won. ****")
                   break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                   printBoard(theBoard)
                   print("\nGame Over.\n")
                   print(" **** " +turn + " won. ****")
                   break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                   printBoard(theBoard)
                   print("\nGame Over.\n")
                   print(" **** " +turn + " won. ****")
                   break
                elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                   printBoard(theBoard)
                   print("\nGame Over.\n")
                   print(" **** " +turn + " won. ****")
                   break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                   printBoard(theBoard)
                   print("\nGame Over.\n")
                   print(" **** " +turn + " won. ****")
                   break

#If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count == 9:
               print("\nGame Over.\n")
               print("It's a Tie!!")

#We have to change the player after every move.
            if turn =='X':
               turn = 'O'
            else:
               turn = 'X'

#Ask players if they wanna play again?
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys: #<-- for each key on the board we make it empty
            theBoard[key] = " "

        game() #<-- calling our function game

if __name__ == "__main__":
    game()
