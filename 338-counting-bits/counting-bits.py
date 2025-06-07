class Solution:
    def countBits(self, n: int) -> List[int]:
        
        l=[]
        # cnt=0
        for i in range(n+1):
            cnt=0
            for j in str(bin(i)):
                if j=='1':
                    cnt+=1
            l.append(cnt)
        return l
