def solution(elements):
    q = elements*2
    resultSet = set()
    
    for i in range(1, len(elements)+1):
        for k in range(len(elements)):
            resultSet.add(sum(q[k:k+i]))    
    
    return len(resultSet)

# 좀 더 빠른 풀이
def solution(elements):
    answer = 0
    
    q = elements*2
    resultSet = set()
    
    for k in range(len(elements)):
        sum = 0
        for i in range(1, len(elements)+1):
            sum += q[k+i]
            resultSet.add(sum)    
    
    return len(resultSet)