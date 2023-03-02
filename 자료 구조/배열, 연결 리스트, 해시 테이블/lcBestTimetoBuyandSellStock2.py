class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        last = prices[0]
        sum = 0
        for i in range(1, len(prices)):
            now = prices[i]
            if (last < now):
                sum += (now - last)
            last = now

        return sum