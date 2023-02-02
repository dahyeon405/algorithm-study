def solution(numbers):
    result = [-1]*len(numbers)
    
    stack = []
    for i in range(len(numbers)):
        if len(stack) == 0 or numbers[i-1]>numbers[i]:
            stack.append(i)
        else:
            while len(stack) > 0 and numbers[stack[-1]] < numbers[i]:
                popped = stack.pop()
                result[popped] = numbers[i]
            stack.append(i)
    
    return result