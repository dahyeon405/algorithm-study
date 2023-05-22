class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n


        q = []
        q.append(0)
        visited[0] = True

        while q:
            _next = q.pop()
            visited[_next] = True

            for r in rooms[_next]:
                if visited[r] is False:
                    q.append(r)
            
        if False in visited: return False
        return True