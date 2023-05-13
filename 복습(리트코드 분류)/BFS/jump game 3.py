class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        q = []
        q.append(start)

        added = set()
        added.add(start)

        while q:
            idx = q.pop()
            if arr[idx] == 0: return True
            k = arr[idx]
            if idx+k < len(arr) and idx+k not in added:
                q.append(idx+k)
                added.add(idx+k)
            if idx-k >= 0 and idx-k not in added:
                q.append(idx-k)
                added.add(idx-k)

        return False
    
# 다른 사람의 풀이
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(index):
            if index < 0 or index >= len(arr) or arr[index] < 0:
                return False
            jump = arr[index]
            arr[index] = -1
            return jump == 0 or dfs(index + jump) or dfs(index - jump)
        return dfs(start)