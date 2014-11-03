# Best Time to Buy and Sell Stock II
# Accepted 228 ms
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <=1:
            return 0
        else:
            income = 0
            for i in range(1,len(prices)):
                if prices[i] > prices[i-1]:
                    income += prices[i] - prices[i-1]
            return income

'''
Input:  [1,2]
Output: -1
Expected:   1


Input:  [1,2]
Output: 0
Expected:   1
'''    