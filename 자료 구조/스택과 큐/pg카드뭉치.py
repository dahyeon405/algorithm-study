from collections import deque

def solution(cards1, cards2, goal):    
    c1 = deque(cards1)
    c2 = deque(cards2)
    
    for i in goal:
        if len(c1) != 0 and c1[0] == i:
            c1.popleft()
        elif len(c2) != 0 and c2[0] == i:
            c2.popleft()
        else: return "No"

    return "Yes"