def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    profit = 0

    buy, sell = prices[0], prices[0]

    for p in prices:
        if buy > p:
            buy = p
            sell = p
            continue
        
        if p > sell:
            sell = p
            profit = max(profit, sell - buy)
        
    return profit
