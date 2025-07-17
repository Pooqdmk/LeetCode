class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        d=Counter(s)
        deletions=len(d.keys())-k
        cnt=0
        while deletions >0:
            mx=100
            k=''
            for key,val in d.items():
                prev=mx
                mx=min(mx,val)
                if prev!=mx:
                    k=key

            d.pop(k)
            cnt+=mx

            deletions-=1
        return cnt

                


    