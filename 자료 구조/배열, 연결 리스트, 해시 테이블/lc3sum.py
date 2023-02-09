class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i-1]): continue
            l = i+1
            r = len(nums)-1
            goal = 0 - nums[i]
            while(l < r):
                sum = nums[r] + nums[l]
                if sum == goal:
                    output.append([nums[i], nums[l], nums[r]])
                    r-=1
                    l+=1
                    while(l < r and nums[l] == nums[l-1]): l+=1
                elif sum > goal:
                    r-=1
                else: l+=1
                    
        return output