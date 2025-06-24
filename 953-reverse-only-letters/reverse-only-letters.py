class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        res=''
        for i in s:
            if i.isalpha():
                res+=i

        res1=res[::-1]
        c=''
        j=0
        for i in s:
            if i.isalpha():
                c+=res1[j]
                j+=1
            else:
                c+=i
        return c
