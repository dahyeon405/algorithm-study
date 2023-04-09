def solution(n, cores):
    # 이분 탐색
    def jobDone(t):
        return sum([t//i + 1 for i in cores])
    
    left = 0
    right = max(cores)*n
    
    while left < right:
        mid = (left+right)//2
        if jobDone(mid) >= n: right = mid
        else: left = mid + 1
    
    t = right
    
    print(t)
        
    remains = n - jobDone(t-1)
    
    last = 0
    for i in range(len(cores)):
        if t%cores[i] == 0: remains -= 1
        if remains == 0: 
            last = i+1
            break
            
    return last