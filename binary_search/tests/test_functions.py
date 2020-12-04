from src.functions import BinarySearch


class Test_BinarySearch:
    value = 4
    ordered_array = [1, 2, 3, 4, 5, 6, 7, 9]
    value_two = 8

    value_three = "r"
    ordered_array_alpha = ["a", "b", "r", "z"]

    def test_binarySearch(self):
        binary_search = BinarySearch(self.value, self.ordered_array)
        assert binary_search.binarySearch() == "index 3"

    def test_binarySearch_alha(self):
        binary_search_three = BinarySearch(self.value_three, self.ordered_array_alpha)
        assert binary_search_three.binarySearch() == "index 2"

    def test_binarySearch_no_value(self):
        binary_serach_two = BinarySearch(self.value_two, self.ordered_array)
        assert binary_serach_two.binarySearch() is None
