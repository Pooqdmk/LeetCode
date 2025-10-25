class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        m = 0
        i,j = 1,1
        while m!=n:
            m+=1
            res+=i
            if m%7 == 0:
                i = j
                j+=1
            i+=1
        return res
