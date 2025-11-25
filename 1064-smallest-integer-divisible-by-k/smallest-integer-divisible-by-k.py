class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2 == 0 or k%5 == 0:
            return -1
        i = 1%k
        cnt = 1
        while i!=0:
            i = (i*10 +1)%k
            cnt+=1
        return cnt


            

