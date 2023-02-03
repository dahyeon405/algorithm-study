# 효율성 실패 (시간초과가 아닌?)
import math
def solution(begin, end):

    def getSecDiv(n):
        if n == 1: return 0
        for i in range(2, math.floor(math.sqrt(n)) + 1):
            if n%i == 0:
                q = n/i
                if q <= 10000000: return n/i # 이 조건을 못 봐서 실패였음
        return 1
    
    result = [0]*(end-begin+1)
    for i in range(begin, end+1):
        result[i-begin] = getSecDiv(i)
        
    return result

