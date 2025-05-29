# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.

class Solution:
    def mySqrt(self, x: int) -> int:
        ## First solution
        # if x <= 1:
        #     return x
        # 
        # res = 1
        # while res * res <= x:
        #     res += 1
        # return res - 1
        if x <= 1:
            return x
        
        left, right = 0, (x // 2)
        while left <= right:
            pivot = left + (right - left) // 2
            n = pivot * pivot
            if n > x:
                right = pivot - 1
            elif n < x:
                left = pivot + 1
            else:
                return pivot
        
        return right
