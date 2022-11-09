import time

print('Welcome to Digwes Quiz')
time.sleep(1)
answer = input('Are you ready for the challenge? (yes/no): ')
time.sleep(2)
print('Before we start please answer using lower-cases!')
score = 0
total_questions = 3

time.sleep(3)
if answer.lower() == 'yes':
    answer = input('Question 1: Who has won the most Balon dors in football? ')
    if answer.lower() == "messi":
        score += 1
        print('Lets go 1 correct')
    else:
        print('LOL you got it wrong')

    time.sleep(2)
    answer = input("Question 2: Who is the richest club in France? ")
    if answer.lower() == "psg":
        score += 1
        print('Lets go another one correct')
    else:
        print('LOL you got it wrong')

    time.sleep(2)
    answer = input("Question 3: How many balon dors has Messi won? ")
    if answer.lower() == "7":
        score += 1
        print('You probs wrote 6 but its 7 because he will win another this year')
    else:
        print('LOL you got it wrong')

time.sleep(2)
print('Thank you for playing this small quiz, you attempted' ,score, 'questions correctly!')
time.sleep(3)
mark = (score/total_questions) * 100
time.sleep(3)
print('Marks obtained:' ,mark)
time.sleep(3)
print('Ciao!')
time.sleep(2)