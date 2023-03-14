class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        sign = 1 if x > 0 else -1
        reversed = ""
        for i in range(len(num)-1, -1, -1):
            if num[i] == "-": continue
            reversed += num[i]
        result = sign*int(reversed)
        return result if -(2**31) < result and result < 2**31 else 0 