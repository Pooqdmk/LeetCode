class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n,m = len(s) , len(t)
        if n!=m:
            return False
        d,l = {},{}
        for i in range(n):
            d[s[i]] = d.get(s[i],0)+1
            l[t[i]] = l.get(t[i],0)+1
        
        for k,v in d.items():
            if k not in l:
                return False
            elif v != l[k]:
                return False
        
        for k,v in l.items():
            if k not in d:
                return False
            elif v != d[k]:
                return False
        return True
        