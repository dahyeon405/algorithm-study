import heapq

def solution(n, k, enemy):
    q = enemy[0:k]
    heapq.heapify(q)
    sum = 0
    for i in range(k, len(enemy)):
        num = enemy[i]
        if q[0] < num:
            sum += heapq.heappop(q)
            heapq.heappush(q, num)
        else:
            sum += num
        if sum > n:
            return i
    
    return len(enemy)