class Solution:
    def smallestNumber(self, n: int) -> int:
        i = n
        while True:
            b = bin(i)[2:]
            if b.count('1') == len(b):
                return i
            i+=1