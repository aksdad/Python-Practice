def highest_product_3(int_list):
    highest = max(int_list[0], int_list[1])
    lowest = min(int_list[0], int_list[1])
    highest_product_of_2 = int_list[0] * int_list[1]
    lowest_product_of_2 = int_list[0] * int_list[1]
    highest_product_of_3 = int_list[0] * int_list[1] * int_list[2]

    for i, v in enumerate(int_list[2:]):
        highest_product_of_3 = max(highest_product_of_3, highest_product_of_2 * v, lowest_product_of_2 * v)
        highest_product_of_2 = max(highest_product_of_2, highest * v, lowest * v)
        lowest_product_of_2 = min(lowest_product_of_2, lowest * v, highest * v)
        highest = max(highest, v)
        lowest = min(lowest, v)

    return highest_product_of_3

if __name__ == '__main__':
    print(highest_product_3([10, 3, 5, 6, 20]))
    print(highest_product_3([-10, -3, -5, -6, -20]))
    print(highest_product_3([1, -4, 3, -6, 7, 0]))