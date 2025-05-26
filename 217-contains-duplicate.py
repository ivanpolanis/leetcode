# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
   def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for n in nums:
            if map.keys().__contains__(n):
                return True
            map[n] = True
        return False
        
