def solution(s):
    def move(s):
        stack = []
        count = 0
        # 우선 110을 전부 다 빼기
        for i in range(len(s)):
            if s[i] == "1":
                stack.append(s[i])
            else:
                if stack[-2:] == ["1", "1"]:
                    count += 1
                    stack.pop()
                    stack.pop()
                else: stack.append(s[i])

        #110 다시 넣어주기
        for i in range(len(stack)):
            if i < (len(stack)-1) and stack[i:i+2] == ["1", "1"]:
                return "".join(stack[:i])+ "110"*count +"".join(stack[i:])
            elif i == len(stack)-1 and stack[i] == "1":
                return "".join(stack[:i])+ "110"*count +"".join(stack[i:])
        return "".join(stack)+"110"*count
    
    result = list(map(move, s))

    return result