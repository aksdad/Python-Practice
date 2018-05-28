def number_of_ways(amount, denominations):
    num_ways_to_make_x = [0] * (amount + 1)
    num_ways_to_make_x[0] = 1

    for denomination in denominations:
        for number in range(denomination, amount + 1):
            other_coin = number - denomination
            num_ways_to_make_x[number] += num_ways_to_make_x[other_coin]

    return num_ways_to_make_x[amount]
if __name__ == '__main__':
    print(number_of_ways(4, [1, 2, 3]))
    print(number_of_ways(4, [5]))
    print(number_of_ways(5, [1,3,5]))