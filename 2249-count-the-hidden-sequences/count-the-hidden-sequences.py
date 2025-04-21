class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        # n=len(differences)
        # l=[0]*(n+1)
        # cnt=0
        # for i in range(lower,upper+1):
        #     l[0]=i
        #     k=1
        #     possible=True
        #     for j in differences:
        #         l[k]=l[k-1]+j
        #         if l[k]<lower or l[k]>upper:
        #             possible=False
        #             break
        #         k+=1
            
        #     if possible:
        #         cnt+=1
        # return cnt
                    
            
        cur,m,n=0,0,0
        for i in differences:
            cur+=i
            m=min(m,cur)
            n=max(n,cur)
        return max(0,(upper-n)-(lower-m)+1)