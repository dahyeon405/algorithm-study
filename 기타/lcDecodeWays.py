# 첨에 dfs로 풀다가 시간초과 남..
# 전형적인 dp 문제
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        # initialization
        if s[0] != "0": dp[0] = 1
        else: return 0
        if len(s) == 1: return dp[0]

        for i in range(1, len(s)):
            if s[i] == "0":
                num = int(s[i-1] + s[i])
                if num <= 0 or num > 26: return 0
                if i == 1: dp[1] = 1
                else: dp[i] = dp[i-2]
                continue
            dp[i] = dp[i-1]
            if s[i-1] != "0" and (s[i-1]+s[i]) <= "26":
                if i == 1: dp[1] = 2
                else: dp[i] += dp[i-2]

        return dp[len(s)-1]