def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) < 2:
        raise IndexError('Need more than 1')

    final_list = [1] * len(int_list)
    product_so_far = 1
    i = 0
    while i < len(int_list):
        final_list[i] = product_so_far
        product_so_far *= int_list[i]
        i += 1

    i = len(int_list) - 1
    product_so_far = 1

    while i >= 0:
        final_list[i] *= product_so_far
        product_so_far *= int_list[i]
        i -= 1

    return final_list


if __name__ == '__main__':
    print(get_products_of_all_ints_except_at_index([3, 2, 4]))
