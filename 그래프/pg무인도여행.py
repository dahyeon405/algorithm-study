import sys
sys.setrecursionlimit(10**5)

def solution(maps):    
    n = len(maps)
    m = len(maps[0])
    board = [["X"]*(m+2) for _ in range(n+2)]
    
    for i in range(n):
        s = maps[i]
        for l in range(m):
            k = s[l]
            if k != "X": k = int(k)
            board[i+1][l+1] = k
    
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def dfs(i, k):
        sum = board[i][k]
        board[i][k] = "X"
        for el in dir:
            x, y = el
            if board[i+x][k+y] != "X":
                sum += dfs(i+x, k+y)
        return sum
    
    result = []
    for i in range(1, n+1):
        for k in range(1, m+1):
            if board[i][k] != "X":
                result.append(dfs(i, k))
   
    if len(result) == 0: return [-1]
    result.sort()
    return result
