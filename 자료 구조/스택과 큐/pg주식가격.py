def solution(prices):
    answer = [0]*len(prices)
    
    stack = []
    for i in range(len(prices)):
        num = prices[i]
        while True: 
            if len(stack) == 0:
                stack.append([num, i])
                break
            if stack[-1][0] > num:
                price, a = stack.pop()
                answer[a] = i-a
            else: 
                stack.append([num, i])
                break
              
    for el in stack:
        num, a  = el
        answer[a] = len(prices) - 1 - a            
    
    return answer