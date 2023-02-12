from collections import deque

def solution(x, y, n):
    # (num, cnt) 형태로 넣기
    q = deque([])
    dp = {}
    q.append((x, 0))
    
    while len(q) > 0:
        num, cnt = q.popleft()
        if num == y: return cnt
        if num*2 <= y: 
            if num*2 not in dp:
                q.append((num*2, cnt+1))
                dp[num*2] = cnt+1
        if num*3 <= y: 
            if num*3 not in dp:
                q.append((num*3, cnt+1))
                dp[num*3] = cnt+1
        if num + n <= y: 
            if num+n not in dp:
                q.append((num+n, cnt+1))
                dp[num+n] = cnt+1
    
    return -1