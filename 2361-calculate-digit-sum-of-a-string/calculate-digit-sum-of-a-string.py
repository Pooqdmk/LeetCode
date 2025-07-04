class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            l=[]
            for i in range(0,len(s),k):
                r=s[i:i+k]
                l.append(str(sum(int(j) for j in r)))

            s=''.join(l)
        return s