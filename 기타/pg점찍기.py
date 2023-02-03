import math
def solution(k, d):
    answer = 0
    
    sum = 0
    for i in range(0, math.floor((d/k)+1)):
        b_max = math.floor(math.sqrt((d**2/k**2) - i**2))
        sum += b_max + 1
    
    return sum