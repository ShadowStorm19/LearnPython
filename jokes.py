from random import randint 
from time import sleep

jokes_list = [
         ("What do you get when you cross a snowman with a vampire?", "Frostbite!"),
         ("What do dentists call an astronaut\'s cavity?", "A black hole!"),
         ("Knock knock.","Who's there?","Interrupting cow.","Interrupting cow wh- MOO")
         ]

jokesLen = len(jokes_list)-1
for i in range(jokesLen):
    jokeNum = randint(0,jokesLen)
    joke = jokes_list[jokeNum]

    for line in joke:
        print(line)
        sleep(1.5)
    print()



