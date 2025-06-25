class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # n=len(word1)
        # m=len(word2)
        # res=''
        # j=0
        # if n <= m:
        #     for i in word1:
        #         res+=i
        #         res+=word2[j]
        #         j+=1
        #     while j<m:
        #         res+=word2[j]
        #         j+=1
        # else:
        #     for i in word2:
        #         res+=i
        #         res+=word1[j]
        #         j+=1
        #     while j<n:
        #         res+=word1[j]
        #         j+=1
        # return res
            
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
