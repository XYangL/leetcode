#Best Time to Buy and Sell Stock
#Accepted 288 ms (1st submit) !!at most one transaction
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        length = len(prices)
        if length <2:
            return 0
        else:
            min_pri = prices[0]
            max_pri = prices[0]
            max_pro = 0
            for pri in prices[1:length]:
                if pri > max_pri:
                    max_pri = pri
                elif pri < min_pri:
                    max_pro = max([max_pro, max_pri-min_pri])
                    min_pri = pri
                    max_pri = pri
            max_pro = max([max_pro, max_pri-min_pri])
            return max_pro

s = Solution()
a = [2,1]#[2,1,2,0,1]#[6,1,3,2,4,7]
print s.maxProfit(a)

