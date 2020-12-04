import random


def gameOptions():
    """
    list of game options

    Returns:
        list: with three options ['rock', 'paper', 'scissors']
    """
    return ["rock", "paper", "scissors"]


def exitOptions():
    """
    game exit options

    Returns:
        list: with three options to exit the game
    """
    return ["q", "quit", "exit"]


def helpOptions():
    """
    game help options

    Returns:
        list: with two options to get help about the game
    """
    return ["h", "help"]


def userInstructions():
    """
    prints out game instructions on the console

    Returns:
        None
    """
    print(
        """
    -> play :: rock, paper or scissors to play
    -> quit :: quit, q or exit to exit
    """
    )


def validateUserInput(user_input):
    """
    validates user input

    Args:
        param(str): primitive data type

    Returns:
        bool: true if param in game options else False
    """
    if user_input in gameOptions():
        return True
    return False


def computerSelection():
    """
    Returns:
        random selection in game options
    """
    return gameOptions()[random.randint(0, (len(gameOptions()) - 1))]


def lowerCaseString(string):
    """
    converts all string character to lowercase

    Args:
        param(str): string to be converted to lowercase

    Returns:
        str: returns string of lowercase characters
    """
    return string.lower()


def gameLogic(pc_option, player_option):
    """
    game logic

    Args:
        param1(str): this is auto generated from list of game options
        param2(str): user option if valid

    Returns:
        str: either -> draw, you win, you lose
    """
    if pc_option == player_option:
        return "Draw"
    else:
        if pc_option == "rock":
            if player_option == "paper":
                return "you win"
            else:
                return "you lose"
        elif pc_option == "paper":
            if player_option == "scissors":
                return "you win"
            else:
                return "you lose"
        elif pc_option == "scissors":
            if player_option == "rock":
                return "you win"
            else:
                return "you lose"
