class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        n=len(s1)
        m=len(s2)
        if n!=m:
            return False
        l=[]
        for i in range(n):
            if s1[i] != s2[i]:
                l.append(i)

        if len(l) == 2:
            res=[0]*n
            res[l[0]]=s1[l[1]]
            res[l[1]]=s1[l[0]]
            for i in range(n):
                if i not in l:
                    res[i] = s1[i]
            res1=[0]*m
            res1[l[0]]=s2[l[1]]
            res1[l[1]]=s2[l[0]]
            for i in range(m):
                if i not in l:
                    res1[i] = s2[i]

        
            if ''.join(res) == s2 or ''.join(res1)==s1:
                return True

            else:
                return False
        return False
            