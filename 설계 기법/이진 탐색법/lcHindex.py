from bisect import bisect_left

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        n = len(citations)
        left = 0
        right = n

        while left < right:
            mid = (left+right)//2 + 1
            idx = bisect_left(citations, mid)
            if (n-idx) >= mid: 
                left = mid
            else:
                right = mid - 1
        
        return left