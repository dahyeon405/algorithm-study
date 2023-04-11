# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # 플로이드 - 워셜 알고리즘
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0
        
        for a, b, d in edges:
            dist[a][b] = d
            dist[b][a] = d

        for j in range(n):
            for i in range(n):
                for k in range(n):
                    _sum = dist[i][j] + dist[j][k]
                    if _sum < dist[i][k]: dist[i][k] = _sum

        citiesCnts = []
        for i in range(len(dist)):
            cnt = -1
            for d in dist[i]:
                if d <= distanceThreshold: cnt += 1
            citiesCnts.append([i, cnt])

        sortedCities = sorted(citiesCnts, key=lambda x: (x[1], -x[0]))
        return sortedCities[0][0]