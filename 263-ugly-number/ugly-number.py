class Solution:
    def isUgly(self, n: int) -> bool:
        if n<=0:
            return False
        # factors = set()
        # while n%2 == 0:
        #     factors.add(2)
        #     n//=2

        # for i in range(3,int(sqrt(n))+1,2):
        #     while n%i == 0:
        #         factors.add(i)
        #         n//=i
        # if n>2:
        #     factors.add(n)
        
        # for i in factors:
        #     if i not in [2,3,5]:
        #         return False
        # return True
        

        for i in [2,3,5]:
            while n%i == 0:
                n//=i
        return n == 1