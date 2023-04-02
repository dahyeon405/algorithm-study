class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for a, b in prerequisites:
            if b in graph: graph[b].append(a)
            else: graph[b] = [a]

        taked = [-1]*numCourses
        
        def isCyclic(node, taked):
            if (taked[node] == 1): return True
            taked[node] = 1
            nextCourses = graph[node] if graph.get(node) else []
            for adj in nextCourses:
                if taked[adj] == 2: continue
                if isCyclic(adj, taked): return True
            taked[node] = 2
            return False

        for i in range(numCourses):
            if taked[i] != -1: continue
            if (isCyclic(i, taked)): return False

        return True