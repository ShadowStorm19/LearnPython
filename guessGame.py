from mymodule import get_valid_num as validNumCheck  # type: ignore
from random import randint 

computerNum = randint(1,20)

name = input('Hello! What is your name: ')
print(f'Well, {name}, I am thinking of a number between 1 and 20.')

iteration = 0

while True:
    guess = validNumCheck('Take a guess \n')
    if  guess < computerNum:
        print('Your guess is too low.')
    elif guess > computerNum:
        print('Your guess is too high.')
    else:
        print(f'Good job {name}, you guessed my number in {iteration} guesses!')
        break
    
    iteration += 1
    if iteration == 6:
        print(f'\nSorry {name}, my number was {computerNum}. Better luck nesxt time.')
        break
    
    print(f'You have {6-iteration} guesses left. \n')
