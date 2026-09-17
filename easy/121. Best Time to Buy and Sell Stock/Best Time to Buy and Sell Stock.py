class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - buy)

        return max_profit
            


# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
sol = Solution()
print(sol.maxProfit(prices))