def solution(triangle):
    height = len(triangle)
    
    dp = [[0]*(i+1) for i in range(height)]
    dp[0][0] = triangle[0][0]
    
    for k in range(1, height):
        for i in range(len(dp[k])):
            cur = triangle[k][i]
            if i == 0 : dp[k][i] = dp[k-1][0] + cur
            elif i == len(dp[k])-1: dp[k][i] = dp[k-1][i-1] + cur
            else: 
                dp[k][i] = max(cur + dp[k-1][i-1], cur + dp[k-1][i])
    
    return max(dp[height-1])