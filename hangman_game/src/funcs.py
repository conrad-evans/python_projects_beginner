import random
from src.words import word_list


def randomWord():
    """
    gets random string in list of strings
    Returns:
        str: random string in list of strings
    """
    word = random.choice(word_list)
    return word.upper()


def play(word):
    """
    game logic for hangman game

    Args:
        param(str): string in all caps
    """
    word_blank = "_" * len(word)
    max_guesses = len(displayHangman()) - 1
    guessed_letters = []

    word_list = list(word)
    word_list_guessed = list(word_blank)

    number_of_tries = 0

    while ("_" in word_list_guessed) or number_of_tries < max_guesses:
        player_input = input("Enter letter: ")
        guessed_letters.append(player_input)
        if isLenOne(player_input) and player_input.isalpha():
            player_input = player_input.upper()
            if player_input in word_list:
                letter_index = word_list.index(player_input)
                word_list[letter_index] == 0
                word_list_guessed[letter_index] = player_input
                print("".join(word_list_guessed))
            else:
                print(displayHangman()[number_of_tries])
                number_of_tries += 1
                if number_of_tries > max_guesses:
                    print("\nFailed the word is", word)
                    break

        else:
            print("Wrong input\n")


def isLenOne(char):
    """
    checks if data type has a length of one

    Args:
        param(str, number, float, list, obj)

    Returns:
        bool: True if data type length is one else false
    """
    if len(char) == 1:
        return True
    return False


def displayHangman():
    """
    Returns:
        list: list of hangman character
    """
    hangman = [
        """
        ---------------
        |
        |
        |
        |
        |
        |
        """,
        """
        ---------------
        |       |
        |       
        |
        |
        |
        |
        """,
        """
        ---------------
        |       |
        |       0
        |
        |
        |
        |
        """,
        """
        ---------------
        |       |
        |       0
        |       |
        |      /|\\
        |
        | 
        """,
        """
        ---------------
        |       |
        |       0
        |       |
        |      /|\\
        |       |
        |      / \\
        """,
    ]
    return hangman
