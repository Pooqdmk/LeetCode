class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n=len(s)
        a=s[:n//2].lower()
        b=s[n//2:].lower()
        l=['a','e','i','o','u']
        cnt1,cnt2=0,0
        for i in a:
            if i in l:
                cnt1+=1
        for i in b:
            if i in l:
                cnt2+=1
        if cnt1==cnt2:
            return True
        else:
            return False
