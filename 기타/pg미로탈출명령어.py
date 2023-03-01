# 계속 고민한 풀이.. 반만 맞음
# 나중에 다시 풀어보자
def solution(n, m, x, y, r, c, k):
    min_path = ""
    diff_x = r-x
    diff_y = c-y
    
    if diff_x > 0:
        min_path += "d"*diff_x
    if diff_y < 0:
        min_path += "l"*abs(diff_y)
    else:
        min_path += "r"*diff_y
    if diff_x < 0:
        min_path += "u"*abs(diff_x)
    
    dir_dict = {"d": (1, 0), "l": (0, -1), "r": (0, 1), "u": (-1, 0)}

    left = k - len(min_path)
    if (left%2 != 0): return "impossible"

    def move(cur_pos, dir):
        next = (cur_pos[0] + dir[0], cur_pos[1] + dir[1])
        if next[0] <= 0 or next[0] > n:
            return False
        if next[1] <= 0 or next[1] > m:
            return False
        return next
    
    result = min_path
    cur_pos = (x, y)
    add = ["du", "lr", "rl", "ud"]
    i = 0
    
    while (left > 0):
        s = ""       
        for el in add:
            if i < len(result):
                s = result[i:i+2]
            elif i == len(result) - 1:
                s = result[i]*2
            if (s == "" or el <= s) and move(cur_pos, dir_dict[el[0]]):
                result = result[:i] + el + result[i:]
                left -= 2
                break

        cur_pos = move(cur_pos, dir_dict[result[i]])
        i += 1
    
    return result