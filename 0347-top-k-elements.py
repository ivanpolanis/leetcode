# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

class Solution:
   def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            if not map.keys().__contains__(n):
                map[n] = 0
            map[n] = map[n] + 1
        
        return [k for k, v in sorted(map.items(), key=lambda item: item[1], reverse=True)[0:k]]
        
