# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        results = [0] * len(temperatures)
        for idx, t in enumerate(temperatures):
            while len(stack) > 0 and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                results[stackInd] = idx - stackInd 
            stack.append((t,idx))
        return results                             
