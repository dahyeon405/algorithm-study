class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        n = len(grid)
        m = len(grid[0])

        def getFinalColumn(idx):

            level = 0
            cur_idx = idx
            isStucked = False
            while level < n:
                if (grid[level][cur_idx] == 1 and (cur_idx+1 == m or grid[level][cur_idx+1] == -1)):
                    isStucked = True
                    break
                if (grid[level][cur_idx] == -1 and (cur_idx == 0 or grid[level][cur_idx-1] == 1)):
                    isStucked = True
                    break
                cur_idx = cur_idx + 1 if grid[level][cur_idx] == 1 else cur_idx - 1
                level += 1
            if isStucked: return -1
            else: return cur_idx

        return [getFinalColumn(i) for i in range(m)]