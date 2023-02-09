# 효율성 실패
def solution(n, k, cmd):
    deleted = []
    status = ['O']*n
    
    curr = k
    for i in cmd:
        arr = i.split(" ")
        if (arr[0] == "D"):
            end = int(arr[1])
            k = 0
            while k < end:
                curr += 1
                if status[curr] == 'O':
                    k += 1
        elif (arr[0] == "U"):
            end = int(arr[1])
            k = 0
            while k < end:
                curr -= 1
                if status[curr] == 'O':
                    k += 1
        elif (arr[0] == "C"):
            deleted.append(curr)
            status[curr] = 'X'
            if curr == n-1: 
                curr -= 1
                while (status[curr] == 'X'):
                    curr -= 1
            else: 
                curr += 1
                while (status[curr] == 'X'):
                    curr += 1
        elif (arr[0] == "Z"):
            last = deleted.pop()
            status[last] = 'O'
            
    answer = "".join(status)
    
    return answer