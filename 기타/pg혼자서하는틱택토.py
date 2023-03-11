def solution(board):
    def isWin(board, w):
        for i in range(3):
            win = True
            for k in range(3):
                if board[i][k] != w: win = False
            if win: return True
                
        for k in range(3):
            win = True
            for i in range(3):
                if board[i][k] != w: win = False
            if win: return True
        
        win = True
        for i in range(3):
            if board[i][i] != w: win = False
        if win: return True

        win = True
        for i in range(3):
            if board[2-i][i] != w: win = False
        if win: return True

        return False
    
    totalO = 0
    totalX = 0
    for i in range(3):
        for k in range(3):
            if board[i][k] == 'O': totalO += 1
            if board[i][k] == 'X': totalX += 1
    
    isOWin = isWin(board, 'O')
    isXWin = isWin(board, 'X')
    
    if (isOWin and totalO == totalX): return 0
    if (isXWin and totalO > totalX): return 0
    if (totalX > totalO): return 0
    if (abs(totalX - totalO) > 1): return 0
    return 1
    