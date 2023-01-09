def MaximumDiscount(N, price):
    price = SortPrices(price)
    N, i = 0, 0
    for i in range(1, len(price) // 3 + 1):
        N += price[3 * i - 1]
    return N


def SortPrices(prices):
    i, j = 0, 0
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] > prices[i]:
                prices[i], prices[j] = prices[j], prices[i]
    return prices
