import heapq
def solution(n, paths, gates, summits):
    
    graph = {}
    for a, b, w in paths:
        if a in graph: graph[a].append((b, w))
        else: graph[a] = [(b, w)]
        if b in graph: graph[b].append((a, w))
        else: graph[b] = [(a, w)]
    
    q = []
    
    dp = [-1]*(n+1)
    
    for el in gates:
        heapq.heappush(q, (0, el))    
        dp[el] = 0
    
    result = [-1, -1]
    while q:
        d, _next = heapq.heappop(q)
        if result[1] != -1 and d > result[1]: break
        if _next not in graph: continue
        
        if _next in summits:
            if result[0] == -1 or _next < result[0]: 
                result = [_next, d]
            continue

        for nb, w in graph[_next]:            
            intensity = max(w, d)
            if dp[nb] == -1 or dp[nb] > intensity:
                dp[nb] = intensity
                heapq.heappush(q, (intensity, nb))      
    
    return result