#To generate a random number we will use Py. module 'random'
import random

#Using random module to generate a number between 1 to 10
#and store it in a variable named number
number = random.randint(1, 10)

#Asking user to put in name and stor in variable called player_name
player_name = input("Hello, What's your name? ")

#Printing player name
print('Okay! '+ player_name+ ' I am guessing a number between 1 and 10:')

# Create a variable and assign 0 to it
number_of_guesses = 0

#While loop
while number_of_guesses < 5: #<-- Giving user 5 attempts to guess number, hence < 5 as our varibale is assigned to 0
    guess = int(input()) #<-- Take input from user and store it in guess variable, convert input from string to integer
    number_of_guesses += 1 #<-- For each wrong guess we increment number_of_guesses

    if guess < number: #<-- If guess is L.T generated number
        print('Your guess is too low')
    if guess > number: #<-- If guess is G.T generated number
        print('Your guess is too high')
    if guess == number: #<-- If guess == to generated number, we terminate the loop completely
        break
if guess == number: #<-- If user gets it right
     print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))