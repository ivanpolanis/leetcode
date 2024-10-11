class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}

        for i, n in enumerate(nums):
            if n in hash_map:
                return [hash_map[n], i]

            comp = target - n
            hash_map[comp] = i

        return [0]
