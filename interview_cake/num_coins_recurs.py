def number_of_ways(amount, denominations):

    num_ways = 0
    for i, coin in enumerate(denominations):
        new_amount = amount - coin
        print(str(coin) + " " + str(new_amount))
        while new_amount > 0:
            num_ways += number_of_ways(new_amount, denominations[(i + 1):])
            new_amount -= coin

        if new_amount == 0:
            num_ways += 1

    return num_ways
if __name__ == '__main__':
    print(number_of_ways(4, [1, 2, 3]))
    print(number_of_ways(4, [5]))
    print(number_of_ways(5, [1,3,5]))