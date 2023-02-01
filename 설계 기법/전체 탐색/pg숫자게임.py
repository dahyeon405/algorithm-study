def solution(A, B):
    
    A.sort()
    B.sort()
    cnt = 0
    k = 0
    
    for i in A:
        while k < len(B):
            if B[k] > i:
                cnt += 1
                k += 1
                break
            k += 1
  
    return cnt