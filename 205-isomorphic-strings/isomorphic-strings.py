class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        d={}
        l={}
        for i,j in zip(s,t):
            if i in d:
                if d[i]!=j:
                    return False
            d[i]=j

            if j in l:
                if l[j]!=i:
                    return False
            l[j]=i
        return True
    
            