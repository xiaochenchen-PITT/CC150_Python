class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        BBDs = [0] # best buy date if sell on day ith
        max_profit = 0
        for i in xrange(1, len(prices)):
        	if prices[i] > prices[BBDs[i-1]]:
        		BBDs.append(BBDs[i-1])
        	else:
        		BBDs.append(i)
        	if prices[i] - prices[BBDs[i]] > max_profit:
        		max_profit = prices[i] - prices[BBDs[i]]
       	return max_profit