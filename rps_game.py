#This is how our computer opponent will play, as I import randint from the random module
from random import randint

#create a list of play options
#3 possible plays I and the computer can make on each turn 'Rock', 'Paper', 'Scissors'
picks = ['Rock', 'Paper', 'Scissors']

#Setting up players; computer and I
#Assign a random pick to the computer using our list 'picks' and the randint function
#Use (0,2) because computers start at 0
#Rock is @ pos. 0, Paper is @ pos. 1, Scissors is @ pos. 2
#Computer has made its play and is waiting for you to take your turn
computer = picks[randint(0,2)]

#Set player to false
player = False

#Once while loop starts, the computer will wait for you to make a move.
#When I take my turn, my status changes from False to True because any value assigned to the variable player makes player True.
while player == False:
#set player to True

    #Player is asked a question and then chooses which they want
    #Use input() func to pass a new value to the Player function
    #Input determines which statement is triggered below
    player = input("Rock, Paper, Scissors?")

    #If my pick and the computers pick are the same its a tie
    #Using nested if/elif/else statements, checking every possible outcome of the game
    #return a message stating the winner, a tie, or an error.
    if player == computer:
        print("Tie!")
    elif player == "Rock": #<-- If I pick 'Rock'
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)

    elif player == "Paper": #<-- If I pick Paper
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)

    elif player == "Scissors": #<-- If I pick Scissors
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)

    #If theres a spelling error you will get this message
    #Use else at end to catch anything that isn’t “Rock”, “Paper” or “Scissors”.
    else:
        print("That's not a valid play. Check your spelling!")

    #Player was set to True, but we want it to be False so the loop continues
    #Finally we reset the player value to False to restart the while loop.
    player = False
    computer = picks[randint(0,2)]
