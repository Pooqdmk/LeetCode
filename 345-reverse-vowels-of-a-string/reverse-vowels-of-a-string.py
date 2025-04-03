class Solution:
    def reverseVowels(self, s: str) -> str:
        d={'a','e','i','o','u'}
        l=[]
        for i in s:
            if i.lower() in d:
                l.append(i)
        l=l[::-1]
        k=0
        r=""
        for i in range(len(s)):
            if s[i].lower() in d:
                r+=l[k]
                k+=1
            else:
                r+=s[i]
        return r