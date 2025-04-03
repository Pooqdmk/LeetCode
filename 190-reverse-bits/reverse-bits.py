class Solution:
    def reverseBits(self, n: int) -> int:
        m=bin(n)[2:].zfill(32)
        t=m[::-1]
        return int(t,2)