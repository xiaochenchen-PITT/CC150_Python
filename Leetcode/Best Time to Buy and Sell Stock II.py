class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    '''hint: greedy'''
        # e.g: [4,2,7,5,9,13,8,5,9]
        # if tomorrow is higher than today ,sell it today and buy tomorrow.
        profit = 0
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i+1]:
                profit -= prices[i] # sell
                profit += prices[i+1]# buy
        return profit