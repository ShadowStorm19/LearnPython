import time
import random

def displayIntro():
    print()
    print('''You are in a land full of dragons. In front of you, you see two caves. 
In one cave, the dragon is friendly and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
    print()
    
def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        cave = input('Which cave will you go into? (1 or 2): ')
    return int(cave)

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == friendlyCave:
        print('Gives you his treasure')
    else:
        print('Gobbles you in one bite!')
    
    print()

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    checkCave(chooseCave())

    playAgain = input('Do you want to play again (yes OR any other key to quit)? ').lower()