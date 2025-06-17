class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # stack=[]
        # j=0
        # # res=''
        # for i in t:
        #     if j<len(s) and stack and stack[-1]==s[j]:
        #         j+=1
        #         stack.pop()

        #     stack.append(i)

        # return len(s)==j-1
        j=0
        for i in t:
            if j<len(s) and i==s[j]:
                j+=1
        return len(s)==j
