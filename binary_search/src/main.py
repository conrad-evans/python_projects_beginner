from src.functions import BinarySearch


def run():
    order_array = input("Enter array: ").split(" ")
    value = input("Enter value: ")

    try:
        order_array = list(map(int, order_array))
    except:
        pass

    try:
        value = int(value)
    except:
        pass

    binary_search = BinarySearch(value, order_array)
    print(binary_search.binarySearch())