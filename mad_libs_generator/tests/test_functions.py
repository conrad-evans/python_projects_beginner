from src.functions import MadLibsGenerator


class Test_MadLibsGenerator:
    words = {
        "place": "zoo",
        "animal": "zebra",
        "country": "zambia",
        "adjective": "huge",
        "color": "red"
    }
    def test_madLibs(self):
        assert MadLibsGenerator(self.words).madLibs() is None
    def test__optionOne(self):
        assert MadLibsGenerator(self.words)._optionOne() is None

    def test__optionTwo(self):
        assert MadLibsGenerator(self.words)._optionTwo() is None

    def test__optionThree(self):
        assert MadLibsGenerator(self.words)._optionThree() is None