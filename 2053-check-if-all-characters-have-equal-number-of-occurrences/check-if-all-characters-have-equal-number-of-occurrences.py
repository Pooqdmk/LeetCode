class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d=Counter(s)
        l=list(d.values())

        for i in range(len(l)-1):
            if l[i] != l[i+1]:

                return False

        return True
