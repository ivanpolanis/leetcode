# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        inner = 0
        for i, n in enumerate(haystack):
            inner = 0
            while inner < len(needle) and i + inner < len(haystack):
                if needle[inner]!= haystack[i + inner]:
                    break
                inner += 1;
            if inner == len(needle):
                return i

        return -1

