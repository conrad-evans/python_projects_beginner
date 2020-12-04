import pytest
from src import functions


def test_gameOPtions():
    game_options = functions.gameOptions()
    assert game_options == ["rock", "paper", "scissors"]


def test_userInstructions():
    user_instructions = functions.userInstructions()
    assert user_instructions is None


def test_validateUserInput():
    correct_input = functions.validateUserInput("rock")
    wrong_input = functions.validateUserInput("virus")
    assert correct_input is True
    assert wrong_input is False


def test_ComputerSelection():
    options = ["rock", "paper", "scissors"]
    # mocker.patch("functions.gameOptions", return_value=options)
    assert functions.computerSelection() in options


def test_lowerCaseString():
    lower_string = functions.lowerCaseString("hElLo WoRlD")
    assert lower_string == "hello world"


def test_gameLogic():
    game_one = functions.gameLogic("rock", "paper")
    game_two = functions.gameLogic("scissors", "paper")
    game_three = functions.gameLogic("paper", "paper")
    assert game_one == "you win"
    assert game_two == "you lose"
    assert game_three == "Draw"
