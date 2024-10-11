class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        val = 0

        for i, c in enumerate(s):
            if i != len(s) - 1:
                if c == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
                    val = val - 2 * hash_map[c]
                if c == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
                    val = val - 2 * hash_map[c]
                if c == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
                    val = val - 2 * hash_map[c]
            val = val + hash_map[c]
        return val
