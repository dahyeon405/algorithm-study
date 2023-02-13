def solution(k, ranges):
    ub = [k]
    num = k
    while num != 1:
        if num%2 == 0:
            num = num//2
        else:
            num = num*3 + 1
        ub.append(num)
    
    
    n = len(ub)
    dp = [0]*n
    
    for i in range(n-1):
        dp[i+1] = round((ub[i] + ub[i+1])/2, 2)
        
    for i in range(1, n):
        dp[i] += dp[i-1]
    
    def getArea(el):
        x, y = el
        y += (n-1)
        if y < x: return -1
        return dp[y] - dp[x]
    
    return list(map(getArea, ranges))