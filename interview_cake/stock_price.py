def get_max_profit(stock_prices_yesterday):
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Profit requires atleast 2 prices')

    l_buy = stock_prices_yesterday[0]
    max_profit = 0

    for i, current_price in enumerate(stock_prices_yesterday[1:]):
        if (current_price - l_buy) > max_profit:
            max_profit = current_price - l_buy

        if l_buy > current_price:
            l_buy = current_price

    return max_profit

if __name__ == '__main__':
    l = [10, 7, 5, 8, 11, 9]
    print(get_max_profit(l))
