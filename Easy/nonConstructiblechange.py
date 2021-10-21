def nonConstructibleChange(coins):
    coins.sort
    change = 0

    for coin in coins:
        if coin > change + 1:
            return change + 1
        change += coin
    return change + 1


x = nonConstructibleChange([0, 2, 3, 4, 5])
print(x)
