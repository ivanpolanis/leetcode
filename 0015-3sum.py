# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) 

        triplets = []

        idx = 0
        while idx < len(nums) - 2:
            if idx > 0 and nums[idx - 1]  == nums[idx]:
                idx += 1
                continue

            a = nums[idx]

            left = idx + 1
            right = len(nums) - 1

            # I want to find a triplet a + b + c = 0.
            # Fixing our a, we just need to find some combination of b + c = -a
            while left < right:
                sum = a + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    triplets.append([a,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

            idx += 1

        return triplets
