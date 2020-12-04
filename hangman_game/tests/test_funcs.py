from src import funcs


def test_randomWord():
    random_word = funcs.randomWord()
    assert type(random_word) is str
    assert random_word.isalpha()
    assert random_word.isupper()

def test_isLenOne():
    is_len_one_one = funcs.isLenOne("a")
    is_len_one_two = funcs.isLenOne("ab")
    is_len_one_three = funcs.isLenOne(["a"])

    assert is_len_one_one
    assert not is_len_one_two
    assert is_len_one_three

def test_displayHangman():
    display_hangman = funcs.displayHangman()
    assert type(display_hangman) is list
    assert len(display_hangman) == 5