class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        extendedboard = [[0]*(n+2)]
        for i in range(m):
            extendedboard.append([0] + board[i] + [0])
        extendedboard.append([0]*(n+2))
        board = extendedboard

        visited = [[False]*(n+2) for _ in range(m+2)]

        def dfs(idx, coord):
            i, k = coord
            if word[idx] != board[i][k]: return False
            if idx == (len(word)-1): return True

            visited[i][k] = True
            dir = [(-1, 0), (0, 1), (0, -1), (1, 0)]
            for x, y in dir:
                if visited[i+x][k+y] is True: continue
                if (dfs(idx+1, (i+x, k+y)) is True): return True
            visited[i][k] = False
            return False

        for i in range(1, m+1):
            for k in range(1, n+1):
                if (dfs(0, (i, k)) is True): return True

        return False
