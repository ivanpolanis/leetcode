# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        anum = 0
        for dig in a  :
            anum = anum * 2 + int(dig)
        bnum = 0
        for dig in b  :
            bnum = bnum * 2 + int(dig)
         
        res = anum + bnum

        if res == 0:
            return '0'

        s = ''
        while res > 0:
            s = str(res % 2) + s
            res = res // 2
        return s

