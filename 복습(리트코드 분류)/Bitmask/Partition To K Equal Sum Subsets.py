class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        nums_sum = sum(nums)
        if nums_sum % k != 0:
            return False
        subset_sum = nums_sum / k
        
        nums.sort(reverse=True)
        visited = [False] * len(nums)
        
        def can_partition(rest_k, cur_sum=0, next_index=0):
            if rest_k == 1:
                return True
            
            if cur_sum == subset_sum:
                return can_partition(rest_k - 1)
            
            for i in range(next_index, len(nums)):
                if not visited[i] and cur_sum + nums[i] <= subset_sum:
                    visited[i] = True
                    if can_partition(rest_k, cur_sum=cur_sum + nums[i], next_index=i + 1):
                        return True
                    visited[i] = False
            return False 
        
        return can_partition(k)