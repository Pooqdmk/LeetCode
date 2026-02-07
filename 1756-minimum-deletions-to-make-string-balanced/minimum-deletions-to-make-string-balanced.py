class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a = [0]*n
        b = [0]*n
        mn = 10**60
        if s[0] == 'a':
            a[0] = 1
        for i in range(1,n):
            if s[i] =='a':
                a[i] = a[i-1]+1
            else:
                a[i] = a[i-1]
        if s[n-1] == 'b':
            b[n-1] = 1
        for i in range(n-2,-1,-1):
            if s[i] == 'b':
                b[i] = b[i+1]+1
            else:
                b[i] = b[i+1]
            
            mn = min(mn,n - (a[i]+ b[i]))
        mn = min(mn, n - (a[n-1]+b[n-1]))
        if n == 1:
            mn = min(mn, n - (a[0]+b[0]))
        return mn