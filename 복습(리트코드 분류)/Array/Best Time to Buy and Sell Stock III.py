# 리트코드
# Array

# Best time to buy and sell stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if cur_min > prices[i]: cur_min = prices[i]
            elif prices[i] - cur_min > max_profit:
                max_profit = prices[i] - cur_min
        return max_profit

# Best time to buy and sell stock 3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prices_front = [0]*len(prices)
        prices_back = [0]*len(prices)

        cur_min = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if cur_min > prices[i]: cur_min = prices[i]
            elif prices[i] - cur_min > max_profit:
                max_profit = prices[i] - cur_min
            prices_front[i] = max_profit

        cur_max = prices[-1]
        max_profit = 0
        for i in range(len(prices)-1, -1, -1):
            if cur_max < prices[i]: cur_max = prices[i]
            elif cur_max - prices[i] > max_profit:
                max_profit = cur_max - prices[i]
            prices_back[i] = max_profit

        total = [prices_front[i] + prices_back[i] for i in range(len(prices))]
        return max(total)
