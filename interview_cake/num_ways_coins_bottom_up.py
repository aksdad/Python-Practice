def number_of_ways(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for denomination in denominations:
        for next_amount in range(denomination, amount + 1):
            other_coin = next_amount - denomination
            ways_of_doing_n_cents[next_amount] += ways_of_doing_n_cents[other_coin]

    return ways_of_doing_n_cents[amount]

if __name__ == '__main__':
    print(number_of_ways(4, [1, 2, 3]))
    print(number_of_ways(4, [5]))
    print(number_of_ways(5, [1,3,5]))