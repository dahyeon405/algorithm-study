def solution(picks, minerals):
    answer = 0
    
    mineralCnt = []
    n = len(minerals)
    
    total = sum(picks)
    
    k = 0
    while k < n and len(mineralCnt) < total:
        cnt = [0, 0, 0]
        for i in range(k, min(n, k+5)):
            if minerals[i] == "diamond": cnt[0] += 1
            elif minerals[i] == "iron": cnt[1] += 1 
            else: cnt[2] += 1
        mineralCnt.append(cnt)
        k += 5
    
    mineralCnt.sort(key = lambda x: (x[0], x[1], x[2]))

    while(sum(picks) > 0 and len(mineralCnt) > 0):
        dia, iron, stone = mineralCnt.pop()
        if picks[0] != 0:
            picks[0] -= 1
            answer += sum([dia, iron, stone])
        elif picks[1] != 0:
            picks[1] -= 1
            answer += sum([dia*5, iron, stone])
        elif picks[2] != 0:
            picks[2] -= 1
            answer += sum([dia*25, iron*5, stone])
    
    return answer