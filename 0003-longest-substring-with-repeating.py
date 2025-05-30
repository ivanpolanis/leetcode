# Given a string s, find the length of the longest substring without duplicate characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        max_len = 0
        map = {}
        while right < len(s):
            char = s[right]
            if char in map:
                if map[char] >= left:
                    left = map[char] + 1
            map[char] = right
            if right - left + 1 > max_len:
                max_len = right - left + 1
            right += 1
        return max_len
