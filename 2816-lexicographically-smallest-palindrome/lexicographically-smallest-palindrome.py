class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        start=0
        end=len(s)-1
        l=list(s)
        while start < end:
            
            if l[start] < l[end]:
                l[end]=l[start]
            else:
                l[start]=l[end]
            start+=1
            end-=1

        return ''.join(l)
            
