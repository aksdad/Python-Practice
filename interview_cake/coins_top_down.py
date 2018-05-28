def number_of_ways_top_down(amount, denominations, current_index):
    if amount == 0:
        return 1

    if amount < 0:
        return 0

    if current_index >= len(denominations):
        return 0

    current_coin = denominations[current_index]
    num_possibilities = 0
    while amount >= 0:
        num_possibilities += number_of_ways_top_down(amount, denominations, current_index + 1)
        amount -= current_coin

    return num_possibilities
def number_of_ways(amount, denominations):
    number_of_ways_top_down(amount, denominations, 0)
if __name__ == '__main__':
    print(number_of_ways(4, [1, 2, 3]))
    print(number_of_ways(4, [5]))
    print(number_of_ways(5, [1,3,5]))