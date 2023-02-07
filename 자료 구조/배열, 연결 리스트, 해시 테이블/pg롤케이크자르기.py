from collections import Counter

def solution(topping):
    answer = 0
    
    toppingCount = dict(Counter(topping))
    total = len(toppingCount)

    myToppings = set()
    
    for i in range(len(topping)):
        t = topping[i]
        if toppingCount[t] == 1: del toppingCount[t]
        else: toppingCount[t] -= 1
        myToppings.add(t)
        if len(toppingCount) == len(myToppings): answer += 1
    
    return answer