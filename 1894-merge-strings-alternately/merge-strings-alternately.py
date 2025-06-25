class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=''
        j=0
        m=len(word2)
        for i in word1:
            res+=i
            if j<m:
                res+=word2[j]
                j+=1
        
        while j<m:
            res+=word2[j]
            j+=1
        return res
