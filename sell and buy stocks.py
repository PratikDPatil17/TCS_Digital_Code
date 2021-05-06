def maxProfit(prices):
    n = len(prices)
    maxcost = 0
    

    if n == 0:
        return 0

    min_price = prices[0]

    for i in range(1, n):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            maxcost = max(maxcost, prices[i]-min_price)
    return maxcost

p = [7,1,5,3,6,4]
t = maxProfit(p)
print(t)
