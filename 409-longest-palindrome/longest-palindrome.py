class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=Counter(s)
        l=list(d.values())
        if len(l)==1:
            return l[0]
        l.sort()
        cnt=0
        if l[0]==1:
            cnt+=1
        else:
            for i in l:
                if i%2!=0:
                    cnt+=1
                    break
        for i in range(len(l)):
            cnt+=2*(l[i]//2)
        return cnt
            