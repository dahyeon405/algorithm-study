from collections import Counter
from itertools import combinations

# 몇 개 틀렸는데 왜 틀렸는지 정말 모르겠다
def solution(user_id, banned_id):
    def isMatched(bid, uid):
        if (len(bid) != len(uid)): return False
        for i in range(len(bid)):
            if bid[i] == "*": continue
            if bid[i] != uid[i]: return False
        return True
    
    idDict = {}
    
    for i in range(len(banned_id)):
        id = banned_id[i]
        idSet = set()
        for k in range(len(user_id)):
            if isMatched(id, user_id[k]): idSet.add(user_id[k])
        idDict[id] = idSet
    
    bids = list(set(banned_id))
    bid_count = dict(Counter(banned_id))
    count = 0
    selected = set()
    def dfs(i):
        nonlocal count
        if i == len(bids):
            count += 1
            return
        
        id = bids[i]
        ids = idDict[id]
        possibleIds = [i for i in ids if i not in selected]
        for j in list(combinations(possibleIds, bid_count[id])):
            selected.update(j)
            dfs(i+1)
            selected.difference_update(j)
        return
    
    dfs(0)
    
    return count