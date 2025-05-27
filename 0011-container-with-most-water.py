# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max = -1

        while left < right:
            area = (height[right] if height[left] > height[right] else height[left]) * (right - left)
            if area > max:
                max = area
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return max
