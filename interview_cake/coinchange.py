def coinchange(coins, amount):
    mem = [float('inf')] * (amount + 1)
    mem[0] = 0

    for i in range(1, amount + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                mem[i] = min(mem[i], mem[i - coins[j]] + 1)
                
    return mem[amount]

if __name__ == '__main__':
    coins = [1, 2, 5]

    print(coinchange(coins, 11))