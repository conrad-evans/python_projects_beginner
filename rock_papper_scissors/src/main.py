from . import functions


def run(running=False):
    running = True
    while running:
        user_input = input("rock, paper, scissors::  ").strip()
        user_input = functions.lowerCaseString(user_input)
        if functions.validateUserInput(user_input):
            computer_selection = functions.computerSelection()
            game_result = functions.gameLogic(computer_selection, user_input)
            print(game_result)
        if user_input in functions.exitOptions():
            running = False
        if user_input in functions.helpOptions():
            functions.userInstructions()
            
