def solution(n):

    dp = [0]*(n//2+1)
    dp[1] = 3
    
    for i in range(2, n//2+1):
        sum = 2
        for k in range(1, i):
            if k == i-1:
                sum += 3*dp[k]
            else: sum += 2*dp[k]
        dp[i] = sum%1000000007
            
    return dp[n//2]