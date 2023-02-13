def solution(n, l, r):

    def calculateOne(n, l, r):
        if n == 2:
            if l <= 2 and r >= 2:
                return r+1 - l -1
            else: return r+1-l
        
        sum = 0
        k = 1
        while k <= 5:
            val = k*(5**(n-2))
            prev = (k-1)*(5**(n-2))
            
            if k == 3 and val > l: # and 뒤에 조건 안 걸어줘서 헤맴.
                l = val
                k += 1
                continue
            if l > r: break
            
            if val > l and val <= r:
                sum += calculateOne(n-1, l-prev, val-1-prev)
                l = val                
            elif val > r:
                sum += calculateOne(n-1, l-prev, r-prev)
                break
            k += 1
        return sum
    
    
    return calculateOne(n+1, l-1, r-1)