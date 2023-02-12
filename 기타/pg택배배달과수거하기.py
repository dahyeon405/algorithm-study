def solution(cap, n, deliveries, pickups):
    sum = 0
    d_next = n-1
    t_next = n-1
    while True:
        d_cap = cap
        t_cap = cap
        d_far = -1
        t_far = -1
        
        d_end = False
        t_end = False
        
        # 배달
        for i in range(d_next, -1, -1):
            if deliveries[i] != 0 and d_far == -1:
                d_far = i
            m = min(deliveries[i], d_cap)
            d_cap -= m
            deliveries[i] -= m
            if d_cap == 0:
                d_next = i
                break
            if i == 0 and deliveries[i] == 0: d_end = True
            
        # 수거
        for i in range(t_next, -1, -1):
            if pickups[i] != 0 and t_far == -1:
                t_far = i
            m = min(pickups[i], t_cap)
            t_cap -= m
            pickups[i] -= m
            if t_cap == 0:
                t_next = i
                break
            if i == 0 and pickups[i] == 0: t_end = True
        
        sum += (max(t_far, d_far)+1)*2
        if d_end and t_end: break
    
    
    return sum