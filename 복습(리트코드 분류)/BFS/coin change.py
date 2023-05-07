import heapq
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0: return 0

        dp = [-1]*(amount+1)
        q = []

        for i in coins:
            heapq.heappush(q, (1, i))
            if i == amount: return 1

        while q:
            cnt, num = heapq.heappop(q)
            for i in coins:
                next_num = num + i
                if next_num > amount: continue
                if dp[next_num] == -1:
                    dp[next_num] = cnt + 1
                    heapq.heappush(q, (cnt+1, next_num))
                if next_num == amount: break

        return dp[amount]