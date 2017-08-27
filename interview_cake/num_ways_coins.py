def number_of_ways(amount, denominations):
    answer = 0
    for index, denomination in enumerate(denominations):
        # print(index)
        amount_left = amount - denomination
        while amount_left > 0:
            answer += number_of_ways(amount_left, denominations[(index + 1):])
            amount_left = amount_left - denomination

        if amount_left == 0:
            answer += 1


    return answer

if __name__ == '__main__':
    print(number_of_ways(4, [1, 2, 3]))
    print(number_of_ways(4, [5]))