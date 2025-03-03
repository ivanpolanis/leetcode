class Solution:
   def majorityElement(self, nums: List[int]) -> int:

        dict = {}

        for n in nums:
            s = str(n)
            if s not in dict.keys():
                dict[s] = 1
            else:
                dict[s] +=1

        return int(max(dict.items(), key=lambda x: x[1])[0])
        
