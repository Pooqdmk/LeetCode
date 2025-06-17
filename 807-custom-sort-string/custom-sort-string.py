class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        # res=''
        # for i in order:
        #     if i in s:
        #         res+=i
        # d=Counter(res)
        # l=Counter(s)
        # for i in s:
        #     if i not in res and d[i]<l[i] :
        #         res+=i

        # return res

        d=Counter(s)
        res=''
        for i in order:
            if i in s:
                res+=i*(d[i])
        l=[]
        for i in s:
            if i not in res and i not in l:
                l.append(i)

        l.sort()
        for i in l:
            res+=i*(d[i])
        return res
