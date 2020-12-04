from random import randint

from .answers import ANSWERS

def magicEightBall():
    input("|-> ")
    print(ANSWERS[randint(0, (len(ANSWERS) - 1))] + "\n")
    playAgain()

def playAgain():
    print("Do you have another question[Y/n]: ")
    question = input("|-> ")

    if question == "yes" or "y":
        magicEightBall()
    elif question == "no" or "n" or "quit" or "q":
        pass
    else:
        print("Invalid response")
        playAgain()
