import random, time
#'choice()' method from random module will be used to
#random words from our word lists
#'sleep()' method from time module will be introduced to
#delays when needed

#Lists used by program to pick words randomly for the players to guess
#Give players the option of picking the category for the word they wanna guess
fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple','cantaloupe', 'grapefruit','jackfruit','papaya']
superHeroes = ['hawkeye', 'robin', 'Galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman', 'aquaman']

#Created game variables to store game stats
userGuesslist = []
userGuesses = []
playGame = True
category = ""
continueGame = "Y"

#Ask for player name then store it in a variable
name = input("Enter your name: ")
#Details about the game before starting it
#time module 'sleep()' method pauses for a few secs between displays
print("Hello", name.capitalize(), "let's start playing Hangman!")
time.sleep(1) #<-- 1 second
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(2)
print("You can guess only one letter at a time. Don't forget to press 'enter key' after each guess.")
time.sleep(3)
print("Let the fun begin!")
time.sleep(1)

#Logic section, allows program to choose a random word from the desired category
while True:
    #Choosing the secret word from the 2 list categories you would like to guess from
    while True:
        #If player presses 'S' = superhero category
        if category.upper() == 'S': #<- Converts input to uppercase
            #A word from the superhero list will be picked randomly using the random
            #the 'random.choice' from 'random' module, the word will be stored in the
            #'secretWord' variable
            secretWord = random.choice(superHeroes)
            break #<-- Leave the loop once right option is chosen
        #If player chooses 'F' = 'fruit' category
        elif category.upper() == 'F':
            secretWord = random.choice(fruits)
            break
        else: #<-- Executed if player chooses 'X' indicating a desire to quit the game + game will end
            category = input("Please select a valid category: F for Fruits / S for Super-Heroes; X to exit: ")

        #Exit option for the game if you decide not to play
        if category.upper() == 'X':
            print("Bye. See you next time!")
            playGame = False #<-- True allows players to continue playing the game and a
            #False allows them to quit the game
            #'playGame' is initialized with the value 'True' at the beginning of the game assuming that the
            #players invoke the program with a desire to play the game.
            #If player opts to quit the game by choosing ‘X’, the boolean ‘playGame’ is set to False which
            #results in bypassing the portion of the program containing the game logic and the game ends
            break

    if playGame:
        secretWordList = list(secretWord)
        attempts = (len(secretWord) + 3) #<-- Attempts is the same length of the word + 3

        #Utility function to print User Guess List
        def printGuessedLetter():
            print("Your Secret word is: " + ''.join(userGuesslist))


        #Adding blank lines to userGuesslist to create the blank secret word
        for n in secretWordList:
            userGuesslist.append('_')
        printGuessedLetter()

        print("The number of allowed guesses for this word is:", attempts)


        #starting the game
        while True:

            print("Guess a letter:")
            letter = input()

            if letter in userGuesses:
                print("You already guessed this letter, try something else.")

            else:
                attempts -= 1
                userGuesses.append(letter)
                if letter in secretWordList:
                    print("Nice guess!")
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    for i in range(len(secretWordList)):
                        if letter == secretWordList[i]:
                            letterIndex = i
                            userGuesslist[letterIndex] = letter.upper()
                    printGuessedLetter()

                else:
                    print("Oops! Try again.")
                    if attempts > 0:
                        print("You have ", attempts, 'guess left!')
                    printGuessedLetter()


            #Win/loss logic for the game
            joinedList = ''.join(userGuesslist)
            if joinedList.upper() == secretWord.upper():
                print("Yay! you won.")
                break
            elif attempts == 0:
                print("Too many Guesses!, Sorry better luck next time.")
                print("The secret word was: "+ secretWord.upper())
                break

        #Play again logic for the game
        continueGame = input("Do you want to play again? Y to continue, any other key to quit")
        if continueGame.upper() == 'Y':
            category = input("Please select a valid categary: F for Fruits / S for Super-Heroes")
            userGuesslist = []
            userGuesses = []
            playGame = True
        else:
            print("Thank You for playing. See you next time!")
            break
    else:
        break