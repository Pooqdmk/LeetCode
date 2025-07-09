class Solution:
    def toHex(self, num: int) -> str:
        if num>0:
            return hex(num)[2:]
        if num==0:
            return '0'
        n=(1 << 32) + num
        return hex(n)[2:]