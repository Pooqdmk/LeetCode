class Solution:
    def fib(self, n: int) -> int:
        a,b = 0,1
        if n == 0:
            return 0
        if n == 1:
            return 1
        i = 2
        while i <= n:
            a,b = b,a+b
            i+=1
        return b


