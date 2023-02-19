from collections import deque

def solution(maps):    
    m = len(maps)
    n = len(maps[0])
 
    def getDist(fr, to):
        
        visited = [[-1]*n for _ in range(m)]
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        q = deque([])
        q.append(fr)
        visited[fr[0]][fr[1]] = 0
        
        while (len(q) > 0):
            next = q.popleft()
            
            nextDist = visited[next[0]][next[1]]
            
            if next == to:
                return nextDist  
        
            for d in dir:
                x = next[0] + d[0]
                y = next[1] + d[1]
                if (x < 0 or x >= m): continue
                if (y < 0 or y >= n): continue
                if (maps[x][y] != "X" and visited[x][y] == -1):
                    visited[x][y] = nextDist+1
                    q.append((x, y))                    
        return -1
        
        
    start, exit, lever = [0, 0, 0]
    for i in range(m):
        for k in range(n):
            if maps[i][k] == "S":
                start = (i, k)
            elif maps[i][k] == "L":
                lever = (i, k)
            elif maps[i][k] == "E":
                exit = (i, k)
    
    StoL = getDist(start, lever)
    LtoE = getDist(lever, exit)
    
    if StoL == -1 or LtoE == -1: return -1
    return StoL + LtoE
    
    return result