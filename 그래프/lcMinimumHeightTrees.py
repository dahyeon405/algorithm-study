# 65/71 통과. 시간 초과
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        graph = {}
        for el in edges:
            a, b = el
            if a in graph: graph[a].append(b)
            else: graph[a] = [b]
            if b in graph: graph[b].append(a)
            else: graph[b] = [a]
        
        def getMaxHeight(root):
            visited = [False]*n

            q = deque([])
            q.append([root, 1])
            visited[root] = True
            
            maxDist = 1
            while len(q)>0:
                nextnode, d = q.popleft()
                if d > maxDist: maxDist = d
                for nb in graph[nextnode]:
                    if not visited[nb]: 
                        q.append([nb, d+1])
                        visited[nb] = True

            return maxDist

        minDist = n
        result = []
        for i in range(n):
            h = getMaxHeight(i)
            if h < minDist: 
                minDist = h
                result = [i]
            elif h == minDist:
                result.append(i)

        return result

# 다른 사람의 풀이
def findMinHeightTrees(self, n, edges):
    if n == 1: return [0] 
    adj = [set() for _ in range(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)

    leaves = [i for i in range(n) if len(adj[i]) == 1]

    while n > 2:
        n -= len(leaves)
        newLeaves = []
        for i in leaves:
            j = adj[i].pop()
            adj[j].remove(i)
            if len(adj[j]) == 1: newLeaves.append(j)
        leaves = newLeaves
    return leaves
	