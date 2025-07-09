class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n=len(str2)
        m=len(str1)
        mx=0
        for i in range(1,m+1):
            if n%i==0 and m%i==0:
                if (n//i)*str1[:i]==str2 and (m//i)*str1[:i]==str1:
                    mx=max(mx,i)
        return str1[:mx]

