def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other indices requires at least 2 numbers')
    # Make a list with the products
    products_so_far = [None] * len(int_list)
    print(products_so_far)
    last_product = 1

    for i in range(len(int_list)):
        products_so_far[i] = last_product
        last_product *= int_list[i]
    print(products_so_far)
    last_product = 1

    for i in range(len(int_list) - 1, -1, -1):
        products_so_far[i] *= last_product
        last_product *= int_list[i]
        
    return products_so_far

if __name__ == '__main__':
    print(get_products_of_all_ints_except_at_index([1, 2, 3]))