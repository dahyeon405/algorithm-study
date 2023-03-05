from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 그래프 만들기
        graph = {}
        for f in flights:
            a, b, price = f
            if a in graph: graph[a].append([b, price])
            else: graph[a] = [[b, price]]

        dist = [float('inf')]*n
        dist[src] = 0

        q = deque([])
        q.append([src, 0])

        cnt = 0
        while cnt <= k:
            newq = deque([])
            while len(q) > 0:
                node, d = q.popleft()
                if node not in graph: continue
                for el in graph[node]:
                    neighbor, d_n = el
                    if dist[neighbor] > d+d_n:
                        dist[neighbor] = d + d_n
                        newq.append([neighbor, dist[neighbor]])
            q = newq
            cnt += 1

        if (dist[dst] == float('inf')): return -1
        else: return dist[dst]