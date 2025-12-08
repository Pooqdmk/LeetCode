class Solution:
    def countTriples(self, n: int) -> int:
        l = [i**2 for i in range(1,n+1)]
        print(l)
        cnt = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                s = sqrt(l[i] + l[j]) 
                if s<=n and s == int(s):
                    cnt+=2
        return cnt
