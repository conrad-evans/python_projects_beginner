from src.functions import Dice


class Test_Dice:

    def test_dice(self):
        assert Dice().dice() is None

    def test__drawOne(self):
        assert Dice()._drawOne() is None

    def test__drawTwo(self):
        assert Dice()._drawTwo() is None

    def test__drawThree(self):
        assert Dice()._drawThree() is None

    def test__drawFour(self):
        assert Dice()._drawFour() is None

    def test__drawFive(self):
        assert Dice()._drawFive() is None

    def test__drawSix(self):
        assert Dice()._drawSix() is None