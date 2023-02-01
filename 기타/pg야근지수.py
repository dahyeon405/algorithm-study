# 내 풀이
def solution(n, works):
    
    works.sort(reverse=True)
    
    sum = 0
    i = 0
    while i < len(works):
        q = n//(i+1)
        diff = works[i]
        if i < len(works) - 1:
            diff = works[i] - works[i+1]
        if q > diff:
            n -= diff*(i+1)
            i+=1
            continue
        else:
            if q < works[i]: 
                r = n%(i+1)
                sum += r*((works[i]-q-1)**2)
                sum += (i+1-r)*((works[i]-q)**2)
            for k in range(i+1, len(works)):
                sum += works[k]**2
            break
        i+=1
    
    return sum     

# 훨씬 간단한 풀이..