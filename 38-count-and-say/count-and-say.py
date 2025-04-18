class Solution:
    def countAndSay(self, n: int) -> str:
        k='1'
        while n-1>0:
            t=''
            cnt=1
            for i in range(len(k)-1):
                if k[i]==k[i+1]:
                    cnt+=1
                else:
                    t+=str(cnt)+k[i]
                    cnt=1
            t+=str(cnt)+k[-1]
            k=t
            n-=1
        return k