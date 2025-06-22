class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        cnt=0
        res=''
        for i in range(len(s)):
            if s[i] == '(':
                c=cnt
                cnt+=1
                if c!=0 and cnt>=1:
                    res+=s[i]
            else:
                c=cnt
                cnt-=1
                if c!=0 and cnt>=1:
                    res+=s[i]

        return res
