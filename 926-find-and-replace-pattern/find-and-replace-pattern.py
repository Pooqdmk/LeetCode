class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res=[]

        for i in words:
            d={}
            l={}
            fine=True
            for j in range(len(i)):
                if i[j] not in d:
                    d[i[j]]=pattern[j]
                    
                else:
                    if d[i[j]] != pattern[j]:
                        fine=False
                        break
            if fine:
                for j in range(len(pattern)):
                    if pattern[j] not in l:
                        l[pattern[j]]=i[j]
                    else:
                        if l[pattern[j]]!=i[j]:
                            fine=False
                            break
            if fine:
                res.append(i)
        return res

            
