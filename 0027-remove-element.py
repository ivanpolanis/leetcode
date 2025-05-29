class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[right] == val:
                right -= 1
            elif nums[left] == val:
                nums[left] = nums[right]
                left += 1; right -= 1
            else:
                left += 1
        if left == right and nums[left] != val:
            left += 1
        return left + 1
        
