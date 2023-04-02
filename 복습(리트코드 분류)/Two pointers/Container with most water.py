# 리트코드
# Array # Two pointer

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_water = 0
        while (l < r):
            max_water = max(max_water, (r-l)*min(height[l], height[r]))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return max_water