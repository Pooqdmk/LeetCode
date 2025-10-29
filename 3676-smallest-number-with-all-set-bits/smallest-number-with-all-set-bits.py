class Solution:
    def smallestNumber(self, n: int) -> int:
        i = n
        while True:
            b = bin(i)[2:]
            if len(set(b)) == 1 and b[0] == '1':
                return i
            i+=1