import math
def solution(distance, rocks, n):
    rocks.append(distance)
    
    rocks.sort()
    
    def isPossible(d):
        cnt = 0
        cur = 0
        end = distance
        i = 0
        while i < len(rocks):
            if rocks[i] - cur < d:
                cnt += 1
            else: cur = rocks[i]
            i += 1
        
        if cnt > n: return False
        else: return True
                
    left = 0
    right = distance
    
    while left < right:
        mid = math.ceil((left+right)/2)
        if (isPossible(mid)):
            left = mid 
        else: right = mid - 1   
    
    return left