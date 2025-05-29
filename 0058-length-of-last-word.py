# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        right = len(s) - 1
        while right > 0 and s[right] == ' ':
            right -= 1
        left = right
        while left >= 0 and s[left] != ' ':
            left -= 1

        if len(s) == 1 and s != ' ':
            return 1

        return right - left
