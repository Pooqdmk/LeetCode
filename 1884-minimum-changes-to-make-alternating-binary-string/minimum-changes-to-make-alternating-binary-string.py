class Solution:
    def minOperations(self, s: str) -> int:
        cnt1=0
        cnt2=0
        n=len(s)
        res1=['0']*n
        res2=['1']*n
        for i in range(n-1):
            if res1[i]=='0':
                res1[i+1]='1'
            else:
                res1[i+1]='0'

            if res2[i]=='0':
                res2[i+1]='1'
            else:
                res2[i+1]='0'

        for i in range(n):
            if s[i]!=res1[i]:
                cnt1+=1
            if s[i]!=res2[i]:
                cnt2+=1
        return min(cnt1,cnt2)