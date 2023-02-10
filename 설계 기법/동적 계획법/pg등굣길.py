def solution(m, n, puddles):    
    board = [[0]*(m+1) for _ in range(n+1)]
    
    board[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles:
                board[i][j] = 0
                continue
            if i == 1:
                if j != 1 and board[i][j-1] != 0:
                    board[i][j] = 1
            elif j == 1: 
                if i != 1 and board[i-1][j] != 0:
                    board[i][j] = 1
            else:         
                board[i][j] = (board[i][j-1] + board[i-1][j])%1000000007

    return board[n][m]