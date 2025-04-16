class Solution:
    def sortSentence(self, s: str) -> str:
        t=s.split(' ')
        l=[0]*len(t)
        for i in t:
            l[int(i[-1])-1]=i[:-1]
        return ' '.join(l)