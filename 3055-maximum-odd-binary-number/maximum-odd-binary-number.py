class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        d=Counter(s)
        return (d['1']-1)*'1'+d['0']*'0'+'1'