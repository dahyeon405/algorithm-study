from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    infoDict = dict()
    
    for i in range(len(info)):
        singleinfo = info[i].split(" ")
        score = int(singleinfo[-1])
        singleinfo = singleinfo[:-1]
        for j in range(5):
            key = combinations(singleinfo, j)
            if key in infoDict:
                infoDict[key].append(score)
            else: infoDict[key] = [score]
        
    def getPeopleCount(q):          
        cond = q.split(" ")
        score = int(cond[-1])
        cond = cond[:-1]
        sortedCond = [i for i in cond if i != "-" and i != "and"]

        key = "".join(sortedCond)
        if key not in infoDict:
            return 0
        scoreList = infoDict[key]
        infoDict[key].sort()
        left = bisect_left(scoreList, score)
        return len(scoreList) - left
        
    
    result = list(map(getPeopleCount, query))
    
    return result