class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s2), len(s1)
        d = Counter(s1)
        for i in range(n-m+1):
            l = Counter(s2[i:i+m])
            found = True
            for k,v in d.items():
                if k in l and l[k] == v:
                    continue
                else:
                    found = False
                    break
            if found:
                return True
        return False
        
