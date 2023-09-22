def maxProfit(prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = prices[0]
        for i in range(len(prices)):
            if prices[i] > buy:
                profit = max(profit, prices[i] - buy)
            else:
                buy = prices[i]
        return profit

print(maxProfit([7,1,5,3,6,4]))
{7 : 0,
 1 : 1,
 5 : 2,
 3 : 3,
 6 : 4,
 4 : 5}