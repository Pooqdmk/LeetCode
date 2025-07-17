class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d=Counter(s)
        l=Counter(target)
        mn=10**6

        for key,val in l.items():
            mn=min(mn,d[key]//val)

        return mn