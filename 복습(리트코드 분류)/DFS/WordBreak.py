# 시간초과
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def dfs(string, idx):
            if idx >= len(string): return True
            _str = ""
            for i in range(idx, len(string)):
                _str += string[i]
                if _str in wordDict:
                    if (dfs(string, i+1)): return True
            return False

        return dfs(s, 0)

# dp 사용!
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [-1]*(len(s))

        def dfs(string, idx):
            if idx >= len(string): return True
            if dp[idx] is False: return False
            _str = ""
            for i in range(idx, len(string)):
                _str += string[i]
                if _str in wordDict:
                    if (dfs(string, i+1)): return True
                    else: dp[i+1] = False
            return False

        result = dfs(s, 0)
        return result