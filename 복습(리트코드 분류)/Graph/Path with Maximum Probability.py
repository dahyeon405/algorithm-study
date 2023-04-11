# 다익스트라 최대 힙

import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # graph
        graph = {}
        for i in range(len(edges)):
            a, b = edges[i]
            d = succProb[i]
            if a in graph: graph[a].append((b, d))
            else: graph[a] = [(b, d)]
            if b in graph: graph[b].append((a, d))
            else: graph[b] = [(a, d)]
        
        q = []
        dist = [-1]*n
        dist[start] = 1
        heapq.heappush(q, (-1, start))
        while q:
            d, nxt = heapq.heappop(q)
            d = -d
            if nxt not in graph: continue
            for nb, nd in graph[nxt]:
                if dist[nb] == -1 or dist[nb] < d*nd:
                    dist[nb] = d*nd
                    heapq.heappush(q, (-dist[nb], nb))

        if dist[end] == -1: return 0
        return dist[end]