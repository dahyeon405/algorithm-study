# 3Sum 풀이를 사용한 내 코드.
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        
        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i-1]):
                i += 1
                continue
            for k in range(i+1, len(nums)-2):
                if (k > i+1 and nums[k] == nums[k-1]):
                    k += 1
                    continue
                l = k+1
                r = len(nums)-1
                goal = target - (nums[i]+nums[k])
                while l < r:
                    sum = nums[l] + nums[r]
                    if sum > goal:
                        r -= 1
                    elif sum < goal:
                        l += 1
                    else:
                        output.append([nums[i], nums[k], nums[l], nums[r]])
                        r -= 1
                        l += 1
                        while (l < r and nums[l] == nums[l-1]): l += 1
        
        return output

# 다른 풀이. 원리는 동일
    def fourSum(self, nums, target):
        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:  # early termination
                return
            if N == 2: # two pointers solve sorted 2-sum problem
                l,r = 0,len(nums)-1
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N
                for i in range(len(nums)-N+1):
                    if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                        findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results