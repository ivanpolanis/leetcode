# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    # O(N^2) pretty slow
    # def recursive(self, n, actual, acum) -> int:
    #     if actual > n:
    #         return acum
    #     if actual == n:
    #         return acum + 1
    #     
    #     acum = self.recursive(n, actual + 1, acum)
    #     acum = self.recursive(n, actual + 2, acum)
    #
    #     return acum
    # def climbStairs(self, n: int) -> int:
    #     return self.recursive(n,0,0)


    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        one, two = 1, 1
        idx = 0
        while idx <= n - 2:
            temp = one + two
            two = one
            one = temp
            idx += 1
        return one

