class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        cnt = 0
        for a in num:
            while cnt < k and len(stack) > 0 and stack[-1] > a:
                stack.pop()
                cnt += 1
            if a == '0' and len(stack) == 0: continue 
            stack.append(a)
   
        while cnt < k and len(stack) > 0:
            stack.pop()
            cnt += 1

        if len(stack) == 0: return "0"
        return "".join(stack)