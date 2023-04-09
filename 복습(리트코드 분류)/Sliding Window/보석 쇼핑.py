def solution(gems):
    gemsSet = set(gems)
    n = len(gemsSet)
     
    left = 0
    right = 0
    
    curGemsDict = { gems[0]: 1 }
    min_length = len(gems)
    result = [0, len(gems)-1]
    
    while left <= right and right < len(gems)-1:        
        # left 앞으로
        if curGemsDict[gems[left]] > 1:
            curGemsDict[gems[left]] -= 1
            left += 1
            
        # right 앞으로
        if len(curGemsDict) < n:
            right += 1
            if gems[right] in curGemsDict:
                curGemsDict[gems[right]] += 1
            else: curGemsDict[gems[right]] = 1
               
        # 다 충족할 경우
        if len(curGemsDict) == n:
            # 기록
            if right-left < min_length:
                result = [left+1, right+1]
                min_length = right-left
            # left 앞으로
            if curGemsDict[gems[left]] == 1: del curGemsDict[gems[left]]
            else: curGemsDict[gems[left]] -= 1
            left += 1
        
        
    return result