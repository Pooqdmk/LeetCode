class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # i=0
        # res=''
        # while i < (len(s))-k:
        #     res+=s[i:i+k][::-1]
        #     i+=k
        #     if i<len(s)-k:
        #         res+=s[i:i+k]
        #         i+=k
        # while i<len(s):
        #     res+=s[i]
        #     i+=1
        # return res

        res=''
        for i in range(0,len(s),2*k):
            res+=s[i:i+k][::-1]
            res+=s[i+k:i+2*k]
        return res
