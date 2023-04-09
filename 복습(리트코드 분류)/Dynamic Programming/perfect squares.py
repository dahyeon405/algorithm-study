import math
# 시간 초과
def numSquares(n):

    dp = [10000]*(n+1)
    for i in range(1, math.floor(math.sqrt(n))+1):
        dp[i*i] = 1
    
    for k in range(1, n+1):
        for i in range(1, k//2 + 1):
            if k == 3: print(dp[k], dp[i] + dp[k-i])
            dp[k] = min(dp[k], dp[i] + dp[k-i])
    
    return dp[n]

# bfs로 해결
import math
from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:

        q = deque([])
        dp = [10000]*(n+1)
        for i in range(1, math.floor(math.sqrt(n))+1):
            dp[i*i] = 1
            q.append([i*i, 1])
        
        ones = [i*i for i in range(1, math.floor(math.sqrt(n))+1)]

        while len(q) > 0:
            num, k = q.popleft()
            if num == n: return k
            for el in ones:
                if num + el <= n and dp[num + el] == 10000:
                    dp[num+el] = k+1
                    q.append([num+el, k+1])

        return dp[n]
