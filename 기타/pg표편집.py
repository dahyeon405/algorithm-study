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

# 고친 풀이
def solution(n, k, cmd):
    deleted = []
    status = ['O']*n 
    dict = {i: [i-1, i+1] for i in range(n)}
    dict[n-1] = [n-2, None]
    dict[0] = [None, 1]
    
    curr = k

    for i in cmd:
        arr = i.split(" ")
        if (arr[0] == "D"):
            end = int(arr[1])
            k = 0
            while k < end:
                curr = dict[curr][1]
                k += 1
        elif (arr[0] == "U"):
            end = int(arr[1])
            k = 0
            while k < end:
                curr = dict[curr][0]
                k += 1
        elif (arr[0] == "C"):
            prev, next = dict[curr]
            deleted.append([curr, prev, next])
            status[curr] = 'X'
            if prev != None:
                dict[prev][1] = next
            if next != None:
                dict[next][0] = prev
            if next == None: 
                curr = dict[curr][0]
            else: 
                curr = dict[curr][1]
        elif (arr[0] == "Z"):
            idx, prev, next = deleted.pop()
            status[idx] = 'O'
            if prev != None:
                dict[prev][1] = idx
            if next != None:
                dict[next][0] = idx
            
    answer = "".join(status)
    
    return answer
