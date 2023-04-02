# 리트코드
# Array

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for l in range(len(nums)):
            if l > 0 and nums[l] == nums[l-1]: continue # 중복 건너뛰기
            m, r = l+1, len(nums)-1
            target = 0 - nums[l]
            while m < r:
                _sum = nums[m] + nums[r]
                if _sum < target: 
                    m += 1
                    while m < r and nums[m] == nums[m-1]: m += 1 # 중복 건너뛰기
                elif _sum > target: 
                    r -= 1
                    while r > m and nums[r] == nums[r+1]: r -= 1
                else: 
                    result.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while m < r and nums[m] == nums[m-1]: m += 1
            l += 1

        return result