def solution(line):
    intersects = set()
    for i in range(len(line)):
        for k in range(i+1, len(line)):
            A, B, E = line[i]
            C, D, F = line[k]
            n = A*D - B*C
            if n == 0: continue
            if (B*F - E*D)%n != 0: continue
            if (E*C - A*F)%n != 0: continue
            intersects.add(((B*F - E*D)//n, (E*C - A*F)//n))
            
    intersects_x = [i[0] for i in intersects]
    intersects_y = [i[1] for i in intersects]
    x_min = min(intersects_x)
    x_max = max(intersects_x)
    y_min = min(intersects_y)
    y_max = max(intersects_y)
    
    board = [["."]*(x_max - x_min + 1) for _ in range(y_max - y_min + 1)]

    for x, y in intersects:
        board[y_max - y][x - x_min] = "*"
    
    answer = []
    
    for row in board:
        answer.append("".join(row))
        
    return answer