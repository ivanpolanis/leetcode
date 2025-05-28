class Solution:
   def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 = m - 1, n - 1
        endidx = m + n - 1

        if n == 0:
            return

        if m == 0:
            idx2 = 0
            while idx2 < n:
                nums1[idx2] = nums2[idx2]
                idx2 += 1
            return

        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] >= nums2[idx2]:
                nums1[endidx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[endidx] = nums2[idx2]
                idx2 -= 1
            endidx -= 1

        while idx2 >= 0:
            nums1[endidx] = nums2[idx2]
            idx2 -= 1
            endidx -= 1

        
