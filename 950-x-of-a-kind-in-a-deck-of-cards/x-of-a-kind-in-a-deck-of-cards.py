class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d=Counter(deck)
        mn=min(d.values())
        if mn == 1:
            return False
        i=2
        while i<=mn:
            a=True
            for k,v in d.items():
                if v%i!=0:
                    a=False
                    break
            if a:
                return True
            i+=1
        return False
