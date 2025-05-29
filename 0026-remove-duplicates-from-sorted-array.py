# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
# - Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# - Return k.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx, act_idx = 0,1
        if len(nums) == 1:
            return 1
        while act_idx < len(nums):
            if nums[idx] != nums[act_idx]:
                idx += 1
                nums[idx] = nums[act_idx]
            act_idx += 1

        return idx + 1
