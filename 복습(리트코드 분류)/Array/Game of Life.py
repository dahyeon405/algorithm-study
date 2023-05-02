class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:

        m = len(board)
        n = len(board[0])

        def getLiveCount(i, k):
            total = 0
            dir = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

            for a, b in dir:
                if (i+a >= 0 and i+a < m and k+b >= 0 and k+b < n):
                    if board[i+a][k+b] == 1 or board[i+a][k+b] == -1 or board[i+a][k+b] == -2: total += 1

            return total


        for i in range(m):
            for k in range(n):
                cnt = getLiveCount(i, k)
                if board[i][k] == 1:
                    if cnt > 3: board[i][k] = -2
                    elif cnt < 2: board[i][k] = -2
                    else: board[i][k] = -1
                elif board[i][k] == 0:
                    if cnt == 3: board[i][k] = -3
                    else: board[i][k] = -4


        for i in range(m):
            for k in range(n):
                if board[i][k] == -1 or board[i][k] == -3: board[i][k] = 1
                else: board[i][k] = 0
                