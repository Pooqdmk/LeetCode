class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        cnt=0
        if cnt==n:
            return True
        if len(f)==1 and f[0]==0:
            return True
        if f[0]==0 and f[1]==0 :
            f[0]=1
            cnt+=1
        for i in range(1,len(f)-1):
            if f[i-1]==0 and f[i]==0 and f[i+1]==0:
                f[i]=1
                cnt+=1
            if cnt==n:
                return True
        if f[-1]==0 and f[-2]==0:
            cnt+=1
        if cnt==n:
            return True
        return False
        
