class Solution:
    def isHappy(self, n: int) -> bool:
        num_set = set()
        num_set.add(n)


        cur_num = n

        result = False
        while True:
            nums = list(map(int, list(str(cur_num)))) 
            _sum = 0
            for el in nums:
                _sum += el**2
            if _sum == 1: 
                result = True
                break
            if _sum in num_set: break
            num_set.add(_sum)
            cur_num = _sum

        return result
    
# 다른 사람의 풀이
# compute sum of squares of digits in n

# while n > 0:
#     digit = n % 10
#     sum_of_squares += digit ** 2
#     n //= 10
