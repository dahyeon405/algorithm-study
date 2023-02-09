# 내 풀이
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        ones = set()
        min = 2**31
        
        for i in nums:
            for k in ones:
                if k < i: return True
            if i < min: min = i
            elif i > min: ones.add(i)
            
            
        return False


# 더 좋은 풀이
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True

        return False