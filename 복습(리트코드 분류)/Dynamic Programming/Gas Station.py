class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        _sum = [gas[i] - cost[i] for i in range(len(gas))]

        dp = _sum[:]
        for i in range(1, len(dp)):
            dp[i] = dp[i-1]+dp[i]

        if (sum(_sum) < 0): return -1

        min_val = min(dp)
        for i in range(len(dp)):
            if dp[i] == min_val: 
                if i == len(dp)-1: return 0
                else: return i+1