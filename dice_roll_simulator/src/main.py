from src.functions import Dice


def run():
    dice = Dice()
    running = "yes"
    while running == "yes" or "y":
        dice.dice()
        running = input("Enter y to roll again or n to exit: ")
