class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s2), len(s1)
        if n < m:
            return False
        d,l = [0]*26, [0]*26
        for i in range(m):
            d[ord(s1[i])-97] +=1
            l[ord(s2[i])-97] +=1
            
        if l == d:
            return True
        for i in range(m,n):
            l[ord(s2[i-m])-97] -=1
            l[ord(s2[i])-97] +=1
            print(l,d)
            if l == d:
                return True
        
        return False