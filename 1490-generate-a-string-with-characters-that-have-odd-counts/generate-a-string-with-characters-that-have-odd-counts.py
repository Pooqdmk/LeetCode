class Solution:
    def generateTheString(self, n: int) -> str:
        if n%2 !=0:
            return 'p'*n
        else:
            return 'p'+('o'*(n-1))