class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        n = 0
        for idx, char in enumerate(s):
            act = dict[char]
            if idx + 1 < len(s) and act < dict[s[idx+1]]:
                n -= act
            else:
                n += act
        return n


