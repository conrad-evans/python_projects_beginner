import random


class Dice:
    """
    dice Class
    """

    def dice(self):
        """
        selects a random number between 1 and 6 and prints the corresponding dice face
        """
        number = random.randint(1, 6)
        if number == 1:
            self._drawOne()
        if number == 2:
            self._drawTwo()
        if number == 3:
            self._drawThree()
        if number == 4:
            self._drawFour()
        if number == 5:
            self._drawFive()
        if number == 6:
            self._drawSix()

    def _drawOne(self):
        """
        prints one on dice
        """
        print("-------------")
        print("|           |")
        print("|     0     |")
        print("|           |")
        print("-------------")

    def _drawTwo(self):
        """
        prints two on dice
        """
        print("-------------")
        print("| 0         |")
        print("|           |")
        print("|         0 |")
        print("-------------")

    def _drawThree(self):
        """
        prints three on dice
        """
        print("-------------")
        print("| 0         |")
        print("|     0     |")
        print("|         0 |")
        print("-------------")

    def _drawFour(self):
        """
        prints four on dice
        """
        print("-------------")
        print("| 0       0 |")
        print("|           |")
        print("| 0       0 |")
        print("-------------")

    def _drawFive(self):
        """
        prints five on dice
        """
        print("-------------")
        print("| 0       0 |")
        print("|     0     |")
        print("| 0       0 |")
        print("-------------")

    def _drawSix(self):
        """
        prints six on dice
        """
        print("-------------")
        print("| 0   0   0 |")
        print("| 0   0   0 |")
        print("| 0   0   0 |")
        print("-------------")