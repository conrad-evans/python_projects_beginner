import random


class MadLibsGenerator:
    def __init__(self, words):
        self.words = words
        self.madLibs()

    def madLibs(self):
        print("\n")
        number = random.randint(1, 3)
        if number == 1:
            self._optionOne()
        if number == 2:
            self._optionTwo()
        if number == 3:
            self._optionThree()

    def _optionOne(self):
        print("Roses are {color}. I saw a {animal} in {place}.".format(**self.words))
        print(
            "{country} is a nice place to visit. Dinner was {adjective}".format(
                **self.words
            )
        )

    def _optionTwo(self):
        print(
            "{animal} is a {adjective} animal natively from {country}.".format(
                **self.words
            )
        )
        print("{place} is {color} from the inside.".format(**self.words))

    def _optionThree(self):
        print(
            "I love {animal}, they have {color} eyes and are {adjective}.".format(
                **self.words
            )
        )
        print("I am from {country}, in a town called {place}".format(**self.words))
