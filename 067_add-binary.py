class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = bin(int(a, base=2) + int(b, base=2))

        return res[2:]
