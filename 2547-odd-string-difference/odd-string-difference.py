class Solution:
    def oddString(self, words: List[str]) -> str:
        l=defaultdict(list)
        res=[]
        for i in words:
            for j in range(len(i)-1):
                res.append(ord(i[j])-ord(i[j+1]))
            
            l[tuple(res)].append(i)
            res.clear()
        
        for val in l.values():
            if len(val) == 1:
                return val[0]
        return 



        