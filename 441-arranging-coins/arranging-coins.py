class Solution:
    def arrangeCoins(self, n: int) -> int:
        s=0
        cnt=-1
        if n==1:
            return 1
        for i in range(1,n+1):
            if s>n:
                break
            s+=i
            cnt+=1
            
        return cnt
