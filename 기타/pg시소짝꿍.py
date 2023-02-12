from itertools import combinations

def solution(weights):
    com = [2, 3, 4]
    combs = list(combinations(com, 2))
    
    weight_map = {}
    
    for i in weights:
        if i in weight_map:
            weight_map[i] += 1
        else:
            weight_map[i] = 1
    
    sum = 0
    keys = list(weight_map.keys())
    keys.sort()
    
    for i in keys:
        # 다른 사람
        for k in combs:
            if (i*k[1])%k[0] != 0: continue
            possible_w = (i*k[1])//k[0]
            if possible_w in weight_map:
                sum += weight_map[i]*weight_map[possible_w]
        
        # 같은 무게
        sum += weight_map[i]*(weight_map[i]-1)/2