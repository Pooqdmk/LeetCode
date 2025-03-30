class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            d1=Counter(s)
            d2=Counter(t)
        else:
            d2=Counter(s)
            d1=Counter(t)
        
        for key,val in d1.items():
            if val!=d2[key]:
                return False
        
        return True

