class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        mx=0
        n=len(s)
        for i in range(n):
            for j in range(i+1,n+1):
                d=Counter(s[i:j])
                exist=True
                for k,v in d.items():
                    if v>2:
                        exist=False
                if exist:
                    mx=max(mx,len(s[i:j]))
        return mx

