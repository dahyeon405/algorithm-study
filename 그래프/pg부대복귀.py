import heapq

def solution(n, roads, sources, destination):

    # 그래프 생성
    graph = {}
    for el in roads:
        a, b = el
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
        if b in graph:
            graph[b].append(a)
        else:
            graph[b] = [a]
    
    # 다익스트라
    def dijkstra(start):
        q = []
        heapq.heappush(q, [0, start])
        dis = [float('INF') for _ in range(n+1)]
        dis[start] = 0 
        
        while len(q) > 0:
            d, v = heapq.heappop(q)
            neighbors = graph.get(v)
            if neighbors == None: continue
            for nb in neighbors:
                if dis[nb] > dis[v] + 1:
                    dis[nb] = dis[v] + 1
                    heapq.heappush(q, [dis[nb], nb])                        
    
        return dis
    
    result = []
    
    dis = dijkstra(destination)
    for i in sources:
        res = dis[i]
        if res == float('INF'):
            res = -1
        result.append(res)
    
    return result