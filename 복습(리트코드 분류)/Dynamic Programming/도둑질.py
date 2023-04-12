def solution(money):
    answer = 0
    
    dp_1 = [0]*(len(money)-1)
    dp_2 = [0]*(len(money)-1)
    
    dp_1[0], dp_1[1] = money[0], money[1]
    dp_2[0], dp_2[1] = money[1], money[2]
    
    for i in range(2, len(money)-1):
        if i >= 3: dp_1[i] = max(dp_1[i-3]+money[i], dp_1[i-2]+money[i])
        elif i == 2: dp_1[i] = dp_1[i-2] + money[i]
    
    for i in range(3, len(money)):
        if i >= 4: dp_2[i-1] = max(dp_2[i-4]+money[i], dp_2[i-3]+money[i])
        elif i == 3: dp_2[i-1] = dp_2[i-3] + money[i]
        
    return max(dp_1[-2], dp_1[-1], dp_2[-1], dp_2[-2])
    
    return answer