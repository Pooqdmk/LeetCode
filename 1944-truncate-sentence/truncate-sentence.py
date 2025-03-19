class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=s.split()
        t=''
        for i in range(k):
            t+=l[i]+' '
        return t.rstrip()
