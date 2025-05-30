# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.


class Solution:
    # For obvious reasons i'm not gonna use int() builtin
    # I'm also not limiting the range to int32 type
    def myAtoi(self, s: str) -> int:
        n = 0
        s = s.strip()  # Removing leading whitespaces
        isValid = False
        isNegative = False

        for c in s:
            if not (c >= "0" and c <= "9") and c != "-":
                return n
            elif c >= "0" and c <= "9":
                isValid = True
                n = n * 10 + ord(c) - ord("0")
            elif c == "-" and not isNegative and not isValid:
                isNegative = True
            elif c == "-":
                return 0
            else:
                return n if not isNegative else -n

        return n if not isNegative else -n
