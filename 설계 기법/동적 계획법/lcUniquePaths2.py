class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        board = [[0]*n for _ in range(m)]
        
        isObstacle = False
        for i in range(m):
            if (obstacleGrid[i][0] == 1):
                isObstacle = True
            if (isObstacle):
                board[i][0] = 0
            else:
                board[i][0] = 1

        isObstacle = False    
        for i in range(n):
            if (obstacleGrid[0][i] == 1):
                isObstacle = True
            if (isObstacle):
                board[0][i] = 0
            else:
                board[0][i] = 1

        for i in range(1, m):
            for k in range(1, n):
                if obstacleGrid[i][k] == 1:
                    board[i][k] = 0
                else: board[i][k] = board[i-1][k] + board[i][k-1]
        
        return board[m-1][n-1]