# 처음 풀이. 시간 초과
import copy
def solution(n):
    
    board = [[0]*n for _ in range(n)]
        
    def put(i, k, board):
        new_board = copy.deepcopy(board)
        new_board[i][k] = 'Q'
        dir = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
        # 검증과 표기 동시에
        for j in range(n):
            if j != k:
                if new_board[i][j] == 'Q': return False
                new_board[i][j] = -1
            if j != i:
                if new_board[j][k] == 'Q': return False
                new_board[j][k] = -1
            for d in dir:
                if j != 0:
                    x, y = i+d[0]*j, k+d[1]*j
                    if x < n and x >= 0 and y < n and y >= 0:
                        if new_board[x][y] == 'Q': return False
                        new_board[x][y] = -1
        return new_board
    
    count = 0
    def dfs(rowIdx, board):
        nonlocal count
        if rowIdx == n: 
            count += 1
            return
        
        for i in range(n):
            if board[rowIdx][i] != -1:
                result = put(rowIdx, i, board)
                if result != False: dfs(rowIdx+1, result)
        return
    
    dfs(0, board)
    
    return count

# 마지막 시간 초과
import copy

def solution(n):
    board = [[0]*n for _ in range(n)]
        
    def canPut(i, k):
        if board[i][k] != 0: return False
        dir = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
        # 검증
        for j in range(n):
            if j != k:
                if board[i][j] == 'Q': return False
            if j != i:
                if board[j][k] == 'Q': return False
            for d in dir:
                if j != 0:
                    x, y = i+d[0]*j, k+d[1]*j
                    if x < n and x >= 0 and y < n and y >= 0:
                        if board[x][y] == 'Q': return False
        return True
    
    count = 0
    
    def dfs(rowIdx):
        nonlocal count
        if rowIdx == n: 
            count += 1
            return
        
        for i in range(n):
            if canPut(rowIdx, i):
                board[rowIdx][i] = 'Q'
                dfs(rowIdx+1)
                board[rowIdx][i] = 0
        return
    
    dfs(0)
    
    return count

# 검증을 더욱 빠르게
import copy

def solution(n):
    columns = set()
    q_s = []
    
    def canPut(i, k):
        # 검증
        if k in columns: return False
        for q in q_s:
            if abs(i-q[0]) == abs(k-q[1]): return False
        return True
    
    count = 0

    
    def dfs(rowIdx):
        nonlocal count
        if rowIdx == n: 
            count += 1
            return
        
        for i in range(n):
            if canPut(rowIdx, i):
                columns.add(i)
                q_s.append([rowIdx, i])
                
                dfs(rowIdx+1)
                
                columns.remove(i)
                q_s.pop()
        return
    
    dfs(0)
    
    return count