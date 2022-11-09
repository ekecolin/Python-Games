# importing the time module
import time
import random

# welcoming the user
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")

# wait for 1 second before moving on
time.sleep(1)

# .5secs before game starts
print("Start guessing...")
time.sleep(0.5)

# here we set the random word to be guessed
words = ("germany", "argentina", "nigeria", "turkey", "pakistan")
word = random.choice(words)
#correct = word

# creates an variable with an empty value
guesses = ''

# determine the number of turns
turns = 10

# Create a while loop

# check if the turns are more than zero
while turns > 0:
    # make a counter that starts with zero
    failed = 0
    # for every character in secret_word
    for char in word:
        # see if the character is in the players guess
        if char in guesses:
            # print then out the character
            print(char,)
        else:
            # if not found, print a dash
            print("_",)
            # and increase the failed counter with one
            failed += 1
            # if failed is equal to zero
    # print You Won
    if failed == 0:
        print(f"Congratulations {name} you win the game!")
# exit the script
        break

# ask the user go guess a character
    guess = input("Guess a character:")
# set the players guess to guesses
    guesses += guess
# if the guess is not found in the secret word
    if guess not in words:
    # turns counter decreases with 1 (now 9)
       turns -= 1
    # print wrong + how many turns/ guesses left
    print(f"Wrong! you have {turns} guesses left")

    # how many turns are left
    #print("You have", + turns, 'more guesses')

# if the turns are equal to zero
if turns == 0:
    # print "You Lose"
    print(f"Unfortunately {name} you lost the game :(")