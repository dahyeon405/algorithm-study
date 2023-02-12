from itertools import product

def solution(users, emoticons):
    rate = [10, 20, 30, 40]
    all_rates = list(product(rate, repeat = len(emoticons)))
    
    def getResult(r):
        count = 0
        sell = 0
        for i in users:
            sum = 0
            for k in range(len(emoticons)):
                if r[k] >= i[0]:
                    sum += (emoticons[k]*(100-r[k]))//100
            if sum >= i[1]:
                count += 1
            else:
                sell += sum
        return [count, sell]
    
    max = [0, 0]
    for r in all_rates:
        count, s = getResult(r)
        if count > max[0]: max = [count, s]
        elif count == max[0] and s > max[1]: max = [count, s]
    
    return max