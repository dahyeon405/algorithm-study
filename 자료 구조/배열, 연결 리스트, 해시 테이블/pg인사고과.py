from bisect import bisect_right
import heapq

def solution(scores):
    y_cnt = [0]*100001
    y_q = []
    
    for i in scores:
        a, b = i
        y_cnt[b]+=1
        heapq.heappush(y_q, -b)
    
    sorted_scores = sorted(scores, key = lambda x: (x[0], -x[1]))
    
    sumArr = []
    invalid = set()
    for i in sorted_scores:
        a, b = i
        while True:
            max = y_q[0]
            if -max in invalid:
                heapq.heappop(y_q)
                continue
            if max >= -b:
                sumArr.append(a+b)
            elif a == scores[0][0] and b == scores[0][1]:
                return -1
            break
       
        y_cnt[b] -= 1
        if y_cnt[b] == 0:
            invalid.add(b)
    
    sorted_sumArr = sorted(sumArr)
    
    wanhoSum = sum(scores[0])
    rightIdx = bisect_right(sorted_sumArr, wanhoSum)

    
    return len(sorted_sumArr) - rightIdx + 1

# 다른 사람의 풀이
def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)
    scores.sort(key=lambda s: (-s[0], s[1]))
    max_company, answer = 0, 1
    for s in scores:
        if wanho[0] < s[0] and wanho[1] < s[1]:
            return -1
        if max_company <= s[1]:
            if wanho_sum < s[0] + s[1]:
                answer += 1
            max_company = s[1]
    return answer