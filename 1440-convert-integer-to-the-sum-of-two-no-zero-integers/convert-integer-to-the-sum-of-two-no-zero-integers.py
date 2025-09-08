class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        i=1
        while True:
            if '0' not in  str(n-i) and '0' not in str(i):
                return [i,n-i]
            i+=1
