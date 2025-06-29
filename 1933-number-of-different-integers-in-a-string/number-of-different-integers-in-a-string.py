class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        
        w=re.sub(r'[a-z]',' ',word)
        l=w.split()
        res=[]
        for i in l:
            if int(i) not in res:
                res.append(int(i))
        return len(res)