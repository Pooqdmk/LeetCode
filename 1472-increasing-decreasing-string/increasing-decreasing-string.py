class Solution:
    def sortString(self, s: str) -> str:
        res=''
        while len(s) > 0:
            l=list(s)
            m=list(sorted(set(l)))
            res+=''.join(m)
            for i in m:
                l.remove(i)
            s=''.join(l)

            l=list(s)
            m=list(sorted(set(l),reverse=True))
            res+=''.join(m)
            for i in m:
                l.remove(i)
            s=''.join(l)

        return res
            