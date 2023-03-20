# 시간은 굿, 공간 복잡도 안 좋음
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        if k == 0: return

        length = len(nums)
        idx = len(nums) - k

        for i in range(length):
            if i < idx:
                nums.append(nums[i])
            else: break

        for i in range(idx, len(nums)):
            nums[i - idx] = nums[i]
        
        n = 0
        while n < len(nums) - k:
            nums.pop()
            n += 1



        """
        Do not return anything, modify nums in-place instead.
        """

# in-place로 변경하라 했지만.. extend 사용하는 방법
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        y = []
        k = k % len(nums)
        y.extend(nums[len(nums)-k:])
        y.extend(nums[:len(nums)-k])
        nums.clear()
        nums.extend(y)