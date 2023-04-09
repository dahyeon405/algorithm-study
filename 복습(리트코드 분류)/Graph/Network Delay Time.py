class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for u, v, w in times:
            if u in graph: graph[u].append([v, w])
            else: graph[u] = [[v, w]]

        dist = [10000 for _ in range(n+1)]
        dist[k] = 0

        for j in range(n):
            updated = False
            for i in range(1, n+1):
                if dist[i] != 10000 and (i in graph):
                    for el, d in graph[i]:
                        if dist[el] > dist[i]+d:
                            dist[el] = min(dist[el], dist[i]+d)
                            updated = True
            if updated is False: break

        dist[0] = 0
        max_dist = max(dist)
        if max_dist == 10000: return -1
        else: return max_dist