class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')]*(len(nums))
        n = len(nums)

        dp[0] = 0
        for i in range(len(nums)):
            if (dp[i] == float('inf')): continue
            j = nums[i]
            for k in range(j+1):
                if (i+k) >= n: break
                dp[i+k] = min(dp[i+k], dp[i]+1)

        return dp[n-1]

# 투 포인터를 활용한 더 좋은 풀이
    def jump(self, nums):
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times