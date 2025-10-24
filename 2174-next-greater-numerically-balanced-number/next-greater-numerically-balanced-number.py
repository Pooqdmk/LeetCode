class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def check(n):
            m = str(n)
            s = set(m)
            for i in s:
                if int(i) != m.count(i) :
                    return False
            return True
        
        mx = 1224444
        for i in range(n+1,mx+1):
            if check(i):
                return i
        return -1