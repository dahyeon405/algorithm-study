class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maxNum = max(nums)
        if maxNum <= 0: return 1
        numSet = set()

        for num in nums:
            numSet.add(num)
        
        for i in range(1, maxNum + 1):
            if i not in numSet:
                return i

        return maxNum + 1