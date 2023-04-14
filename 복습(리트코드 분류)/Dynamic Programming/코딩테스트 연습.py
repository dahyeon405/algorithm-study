def solution(alp, cop, problems):

    maxAlp = max(max([i[0] for i in problems]), alp)
    maxCop = max(max([i[1] for i in problems]), cop)
    
    # dp[a][b]: alp a, cop b 도달 최소 시간
    dp = [[float('inf')]*(maxCop+1) for _ in range(maxAlp+1)]
    
    dp[alp][cop] = 0
    
    for i in range(alp, maxAlp+1):
        for k in range(cop, maxCop+1):
            if k+1 <= maxCop: dp[i][k+1] = min(dp[i][k+1], dp[i][k]+1)
            if i+1 <= maxAlp: dp[i+1][k] = min(dp[i+1][k], dp[i][k]+1)
            
            for el in problems:
                if el[0] <= i and el[1] <= k:
                    i_alp, i_cop, t = el[2:5]
                    new_alp = min(i+i_alp, maxAlp)
                    new_cop = min(k+i_cop, maxCop)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][k] + t)
    
    return dp[maxAlp][maxCop]