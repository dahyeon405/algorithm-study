import sys
sys.setrecursionlimit(10**6)
# 스택 크기 바꿔줘야 해서 좋은 풀이는 아님.
def solution(grid):
    m = len(grid)
    n = len(grid[0])
    
    dir_r = {'t': 'l', 'r': 't', 'l': 'd', 'd': 'r'}
    dir_l = {'t': 'r', 'r': 'd', 'l': 't', 'd': 'l'}
    dir_s = {'t': 'd', 'd': 't', 'r': 'l', 'l': 'r'}
    
    dir = ['t', 'd', 'r', 'l']
    add = {'t': (-1, 0), 'd':(1, 0), 'r':(0, 1), 'l':(0, -1)}
    
    # 그래프 생성
    board = [[0]*n for _ in range(m)]
    for i in range(m):
        for k in range(n):
            board[i][k] = {'t': -1, 'd': -1, 'r': -1, 'l': -1}
    
    result = []
    def dfs(i, k, dir, dis):
        # 인덱스 초과 보정
        if i >= m: i -= m
        elif i < 0 : i += m
        if k >= n: k -= n
        elif k < 0: k += n
        
        # dir은 들어오는 방향, 현재 노드 기준.
        if board[i][k][dir] != -1:
            result.append(dis)
            return
        # 방문 표기
        board[i][k][dir] = 1
        
        # 다음 방문
        next_dir = ''
        if grid[i][k] == 'S':
            next_dir = dir_s[dir]
        elif grid[i][k] == 'L':
            next_dir = dir_l[dir]
        elif grid[i][k] == 'R':
            next_dir = dir_r[dir]
        
        x, y = add[next_dir]
        dfs(i+x, k+y, dir_s[next_dir], dis+1)
        
    for i in range(m):
        for k in range(n):
            for j in dir:
                if board[i][k][j] == -1:
                    dfs(i, k, j, 0)
    
    result.sort()
    return result

# while문으로 변경
def solution(grid):
    m = len(grid)
    n = len(grid[0])
    
    dir_r = {'t': 'l', 'r': 't', 'l': 'd', 'd': 'r'}
    dir_l = {'t': 'r', 'r': 'd', 'l': 't', 'd': 'l'}
    dir_s = {'t': 'd', 'd': 't', 'r': 'l', 'l': 'r'}
    
    dir = ['t', 'd', 'r', 'l']
    add = {'t': (-1, 0), 'd':(1, 0), 'r':(0, 1), 'l':(0, -1)}
    
    # 그래프 생성
    board = [[0]*n for _ in range(m)]
    for i in range(m):
        for k in range(n):
            board[i][k] = {'t': -1, 'd': -1, 'r': -1, 'l': -1}
    
    def dfs(i, k, dir, dis):
        # dir은 들어오는 방향, 현재 노드 기준.
        if board[i][k][dir] != -1:
            result.append(dis)
            return -1
        # 방문 표기
        board[i][k][dir] = 1
        
        # 다음 방문
        next_dir = ''
        if grid[i][k] == 'S':
            next_dir = dir_s[dir]
        elif grid[i][k] == 'L':
            next_dir = dir_l[dir]
        elif grid[i][k] == 'R':
            next_dir = dir_r[dir]
        
        x, y = add[next_dir]
        i += x
        k += y
        
        # 인덱스 초과 보정
        if i >= m: i -= m
        elif i < 0 : i += m
        if k >= n: k -= n
        elif k < 0: k += n
        
        return (i, k, dir_s[next_dir], dis+1)
        
    result = []
    for i in range(m):
        for k in range(n):
            for j in dir:
                if board[i][k][j] == -1:
                    x, y, cur_dir, dis = i, k, j, 0
                    while True:
                        res = dfs(x, y, cur_dir, dis)
                        if res == -1:
                            break
                        x, y, cur_dir, dis = res
    
    result.sort()
    return result