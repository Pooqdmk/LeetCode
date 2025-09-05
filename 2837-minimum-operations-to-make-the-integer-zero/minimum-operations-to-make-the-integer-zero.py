class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        
        k=1
        while True:
            s=num1 - k*num2
            if s < 0:
                break
            if bin(s)[2:].count('1') <= k and k<=s:
                return k
            if k > s:
                break
            k+=1
        return -1

