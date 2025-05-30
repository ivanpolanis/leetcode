# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}

        for idx, c in enumerate(s):
            if c in map:
                map[c] = -1
            else:
                map[c] = idx

        for c in s:
            if map[c] != -1:
                return map[c]

        return -1
