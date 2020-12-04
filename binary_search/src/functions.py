class BinarySearch:
    def __init__(self, value, order_array):
        """
        binary value class

        Args:
            param1(int): single int character
            parma2(array): ordered array
        """
        self.value = value
        self.order_array = order_array

    def binarySearch(self):
        """
        binary search algorithm
        """
        lower_bound = 0
        upper_bound = len(self.order_array) - 1

        while lower_bound <= upper_bound:
            mid_point = int((lower_bound + upper_bound) / 2)
            mid_point_value = self.order_array[mid_point]

            if self.value < mid_point_value:
                upper_bound = mid_point - 1

            elif self.value > mid_point_value:
                lower_bound = mid_point + 1

            elif self.value == mid_point_value:
                return "index " + str(mid_point)

        return None
