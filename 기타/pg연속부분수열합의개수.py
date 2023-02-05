def solution(elements):
    q = elements*2
    resultSet = set()
    
    for i in range(1, len(elements)+1):
        for k in range(len(elements)):
            resultSet.add(sum(q[k:k+i]))    
    
    return len(resultSet)