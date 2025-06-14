class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l=s1.split(' ')
        m=s2.split(' ')

        c1=Counter(l)
        c2=Counter(m)

        res=[]
        for i in l:
            if i not in m and c1[i]==1:
                res.append(i)
        
        for j in m:
            if j not in l and c2[j]==1 :
                res.append(j)
        return res
